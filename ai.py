import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

st.set_page_config(page_title="CurricuForge AI", layout="wide")

st.title("🎓 CurricuForge AI")
st.subheader("AI Curriculum Generator")

skill = st.text_input("Enter Skill (Example: Python, Machine Learning)")
goal = st.text_input("Learning Goal (Example: Become Job Ready in 3 months)")

if st.button("Generate Curriculum"):

    with st.spinner("Generating AI Curriculum..."):

        prompt = f"""
You are an expert curriculum designer.

Create a structured learning roadmap.

Skill: {skill}
Goal: {goal}

Format the response clearly using Markdown.

Include these sections:

1. Overview

2. Weekly Learning Roadmap Table
Columns:
Week | Topics | Practice | Outcome

3. Learning Stages
Beginner
Intermediate
Advanced

4. Learning Flow
Represent the journey like:
Start -> Basics -> Practice -> Projects -> Mastery

5. Practice Exercises

6. Final Project Idea

7. Useful Resources

Make the output clean, structured, and beginner friendly.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

        st.success("Curriculum Generated Successfully!")

        st.markdown(result)