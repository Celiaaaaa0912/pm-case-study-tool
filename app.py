import streamlit as st
from google import genai
import os

# Config
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Page setup
st.set_page_config(page_title="PM Case Study Analyzer", page_icon="🔍")
st.title("🔍 PM Case Study Analyzer")
st.markdown("Enter a product name to get an instant PM case study analysis.")

# Input
app_name = st.text_input("Product name (e.g. Notion, Duolingo, Airbnb)")

if st.button("Analyze") and app_name:
    with st.spinner("Analyzing..."):

        prompt = f"""
You are a senior Product Manager. Analyze the product "{app_name}" and return exactly this structure:

## 👥 User Pain Points
1. [pain point 1]
2. [pain point 2]
3. [pain point 3]

## ⚔️ Competitor Comparison
| Feature | {app_name} | Competitor A | Competitor B |
|--------|-----------|-------------|-------------|
| [feature 1] | ... | ... | ... |
| [feature 2] | ... | ... | ... |
| [feature 3] | ... | ... | ... |

## 💡 Product Improvement Suggestions
1. [suggestion 1 with reasoning]
2. [suggestion 2 with reasoning]
3. [suggestion 3 with reasoning]

## 📊 PM Opportunity Score
Rate the product opportunity from 1-10 and explain why in 2 sentences.

Be specific, concise, and think like a PM.
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        st.markdown(response.text)
