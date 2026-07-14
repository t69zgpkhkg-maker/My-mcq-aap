import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="AI MCQ Generator", page_icon="📸")
st.title("📸 AI MCQ Generator From Photo")
st.write("Kisi bhi book ya notes ki photo upload karein aur MCQs taiyaar karein!")

# Sidebar me API key input
api_key = st.sidebar.text_input("Apni Gemini API Key yahan dalein:", type="password")

uploaded_file = st.file_uploader("Photo select karein (PNG, JPG, JPEG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Photo", use_container_width=True)
    
    num_questions = st.slider("Kitne Questions chahiye?", min_value=3, max_value=10, value=5)
    
    if st.button("✨ MCQs Taiyaar Karein"):
        if not api_key:
            st.error("Kripya Sidebar me apni Gemini API Key dalein!")
        else:
            with st.spinner("AI photo ko padh raha hai aur MCQs bana raha hai..."):
                try:
                    # Naye Google GenAI SDK ka bilkul sahi format
                    client = genai.Client(api_key=api_key)
                    
                    prompt = f"Is image ke text ko achhe se samjho aur isse {num_questions} Multiple Choice Questions (MCQs) banao. Har question ke 4 options (A, B, C, D) hone chahiye aur end me Correct Answer aur chota sa explanation hona chahiye. Language Hinglish (Hindi + English mix) rakhein."
                    
                    # Naya official 2026 stable model aur format
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=[image, prompt]
                    )
                    
                    st.success("🎉 Aapke MCQs Taiyaar Hain!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Koyi galti hui: {e}")
