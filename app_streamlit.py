import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Page Config
st.set_page_config(page_title="StudyBuddy.AI Lite", page_icon="🎓")

if not api_key:
    st.error("Please add your GEMINI_API_KEY to the .env file or Streamlit Secrets.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("🎓 StudyBuddy.AI Lite")
    st.markdown("---")

    # Sidebar
    st.sidebar.header("Navigation")
    choice = st.sidebar.radio("Go to", ["Flashcard Generator", "Quick Explainer", "Study Planner"])

    if choice == "Quick Explainer":
        st.subheader("💡 AI Quick Explainer")
        topic = st.text_input("What concept do you want to learn today?")
        if st.button("Explain"):
            if topic:
                with st.spinner("AI is thinking..."):
                    response = model.generate_content(f"Explain {topic} in simple terms with examples.")
                    st.write(response.text)
            else:
                st.warning("Please enter a topic.")

    elif choice == "Flashcard Generator":
        st.subheader("🗂️ Flashcard Generator")
        context = st.text_area("Paste your study text here:")
        if st.button("Generate"):
            if context:
                with st.spinner("Creating flashcards..."):
                    prompt = f"Generate 5 Q&A pairs for flashcards from this text: {context}. Format: Question: ... Answer: ..."
                    response = model.generate_content(prompt)
                    st.write(response.text)

    elif choice == "Study Planner":
        st.subheader("📅 AI Study Planner")
        topic = st.text_input("Course/Subject Name:")
        deadline = st.date_input("When is your exam/deadline?")
        if st.button("Plan Now"):
            with st.spinner("Creating your custom roadmap..."):
                prompt = f"Create a study schedule for {topic} until {deadline}."
                response = model.generate_content(prompt)
                st.write(response.text)

st.sidebar.markdown("---")
st.sidebar.info("This is a Streamlit version of StudyBuddy.AI.")
