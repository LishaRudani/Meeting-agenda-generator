import streamlit as st
import requests

# Backend endpoint
BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Meeting Agenda Generator", layout="centered")
st.title("🧠 AI-Powered Meeting Agenda Generator")

# User inputs
title = st.text_input("Meeting Title")
topics = st.text_area("List of Topics (comma-separated)")
duration = st.text_input("Total Duration (e.g., 60 minutes)")

if st.button("Generate Agenda"):
    if not title or not topics or not duration:
        st.error("Please fill in all the fields.")
    else:
        with st.spinner("Generating agenda..."):
            response = requests.post(f"{BACKEND_URL}/generate-agenda", json={
                "title": title,
                "topics": topics,
                "duration": duration
            })
            if response.status_code == 200:
                agenda = response.json().get("agenda")
                st.session_state["agenda"] = agenda
                st.success("Agenda generated successfully!")
            else:
                st.error("Failed to generate agenda. Please try again.")

# Editable agenda text area
if "agenda" in st.session_state:
    st.subheader("✍️ Customize Your Agenda")
    edited_agenda = st.text_area("Generated Agenda", value=st.session_state["agenda"], height=300)

    if st.button("Download as PDF"):
        with st.spinner("Preparing PDF..."):
            params = {"title": title}
            pdf_response = requests.get(f"{BACKEND_URL}/download-pdf", params=params)

            if pdf_response.status_code == 200:
                st.download_button(
                    label="📥 Click to Download PDF",
                    data=pdf_response.content,
                    file_name=f"{title}.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Failed to download PDF. Please try again.")
