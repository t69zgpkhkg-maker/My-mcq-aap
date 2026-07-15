import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="AI MCQ Generator", page_icon="📸")
st.title("📸 AI MCQ Generator From Photo")

api_key = st.sidebar.text_input("Apni Gemini API Key dalein:", type="password")
uploaded_file = st.file_uploader("Photo select karein...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Photo", use_container_width=True)
    num_questions = st.slider("Kitne Questions chahiye?", min_value=3, max_value=10, value=5)
    
    if st.button("✨ MCQs Taiyaar Karein"):
        with st.spinner("AI Kaam kar raha hai..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"Is image se {num_questions} MCQs banao options A, B, C, D ke sath aur correct answer bhi do. Language Hinglish rakho."
                
                # Bina kisi version lafde ke auto-pick karne wala standard model string
                response = client.models.generate_content(
                    model= genai.GenerativeModel("gemini-2.0-flash")

                    contents=[image, prompt]
                )
                st.success("🎉 Taiyaar Hain!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Koyi galti hui: {e}")
