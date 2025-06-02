from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import os
from fastapi.responses import FileResponse
from generate_pdf import create_pdf
from groq_integration import generate_agenda_llm

app = FastAPI()
DB = 'agendas.db'

class AgendaRequest(BaseModel):
    title: str
    topics: str
    duration: str

@app.on_event("startup")
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS agendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            topics TEXT,
            agenda TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.post("/generate-agenda")
def generate_agenda(req: AgendaRequest):
    if not all([req.title.strip(), req.topics.strip(), req.duration.strip()]):
        return {"error": "All fields are required"}

    agenda = generate_agenda_llm(req.title, req.topics, req.duration)

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO agendas (title, topics, agenda, timestamp) VALUES (?, ?, ?, ?)",
              (req.title, req.topics, agenda, datetime.now().isoformat()))
    conn.commit()
    conn.close()

    return {"agenda": agenda}

@app.get("/download-pdf")
def download_pdf(title: str = Query(...)):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT agenda FROM agendas WHERE title=? ORDER BY id DESC LIMIT 1", (title,))
    result = c.fetchone()
    conn.close()

    if not result:
        return {"error": "Agenda not found"}

    file_path = create_pdf(title, result[0])
    return FileResponse(file_path, filename=f"{title}.pdf", media_type='application/pdf')
