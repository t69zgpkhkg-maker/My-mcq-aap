import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="AI MCQ Generator", page_icon="📸")
st.title("📸 AI MCQ Generator From Photo")
st.write("Kisi bhi book ya notes ki photo upload karein aur MCQs taiyaar karein!")

# Sidebar me API key input
api_key = st.sidebar.text_input("Apni Gemini API Key yahan dalein:", type="password")

uploaded_file = st.file_uploader("Photo select karein (PNG, JPG, JPEG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is
