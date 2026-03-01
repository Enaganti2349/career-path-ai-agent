import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

st.set_page_config(page_title="CareerPath AI Agent", page_icon="💼")

st.title("💼 CareerPath AI Agent (Groq + LLaMA 3.1)")
st.write("AI-powered career recommendation system.")

# User Inputs
skills = st.text_input("Enter your skills:")
education = st.text_input("Enter your education:")
interests = st.text_input("Enter your interests:")

if st.button("Get Recommendation"):

    if not skills or not education or not interests:
        st.warning("⚠ Please fill all fields.")
    else:
        prompt = f"""
You are a professional AI career advisor.

User Profile:
Skills: {skills}
Education: {education}
Interests: {interests}

Provide:
1. Best career roles
2. Required skills
3. Step-by-step learning roadmap.
Make the response structured and clear.
"""

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert career guidance AI."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=600
            )

            result = response.choices[0].message.content

            st.success("🎯 AI Career Recommendation:")
            st.write(result)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")