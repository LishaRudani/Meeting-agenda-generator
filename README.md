# Task1
# 🧠 AI-Powered Meeting Agenda Generator

This application allows users to input a meeting title, list of topics, and meeting duration, and generates a professional meeting agenda using a Large Language Model (LLM) from Groq (e.g., LLaMA3). The app also allows PDF download and agenda editing.

---

## 🌐 Live Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend  | FastAPI |
| LLM      | Groq API (e.g., LLaMA3-8b) |
| Database | SQLite |
| Hosting  | AWS EC2 |

---

## Project Setup Instructions

###  Clone or Upload the Project

```bash
git clone https://github.com/LishaRudani/meeting-agenda-generator.git
cd meeting-agenda-generator
sudo apt update
sudo apt install python3-pip -y
pip3 install virtualenv

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

fastapi
uvicorn
streamlit
requests
reportlab
pydantic
python-dotenv

export GROQ_API_KEY="your_groq_api_key"
echo 'export GROQ_API_KEY="your_groq_api_key"' >> ~/.bashrc
source ~/.bashrc
User (Browser)
     |
     v
 Streamlit (Frontend) ←→ FastAPI (Backend)
     |                        |
     v                        v
  PDF Download        Groq API (LLM), SQLite DB

