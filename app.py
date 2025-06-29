# shodan_gpt_dashboard.py

import streamlit as st
import pandas as pd
import shodan
import openai
import os
from dotenv import load_dotenv
load_dotenv()

from src.risk_assessor import assess_risk as assess_risk_with_gpt

# --- CONFIG ---
SHODAN_API_KEY = st.secrets["SHODAN_API_KEY"]  # store in .streamlit/secrets.toml
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

# --- SIDEBAR ---
st.sidebar.title("🔐 API Keys")
st.sidebar.info("Add your API keys in `.streamlit/secrets.toml`:")
st.sidebar.code("""
[default]
SHODAN_API_KEY = "your-shodan-key"
OPENAI_API_KEY = "your-openai-key"
""", language="toml")

st.sidebar.text(f"OpenAI key starts with: {OPENAI_API_KEY[:5]}")

# --- TITLE ---
st.title("🔍 Shodan + GenAI Risk Analyzer")
st.markdown("""
Search the internet for exposed devices using Shodan,  
and analyze their risk using OpenAI's GPT.
""")

# --- INPUT FORM ---
with st.form("shodan_form"):
    query = st.text_input("🔎 Shodan Search Query", value="ftp anonymous login")
    limit = st.slider("Number of results", 1, 20, 5)
    submitted = st.form_submit_button("Scan + Analyze")

# --- MAIN LOGIC ---
def search_shodan(query, limit):
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.search(query, limit=limit)
    return results['matches']

def classify_risk_level(text):
    text = text.lower()
    if any(x in text for x in ["anonymous login ok", "admin access", "exposed"]):
        return "🔴 High"
    elif any(x in text for x in ["login required", "no anonymous", "restricted"]):
        return "🟠 Medium"
    elif any(x in text for x in ["service ready", "info only"]):
        return "🟡 Low"
    else:
        return "🔵 Info"

# --- RUN IF SUBMITTED ---
if submitted:
    try:
        st.info(f"Searching for: `{query}`...")
        data = search_shodan(query, limit)

        rows = []
        for d in data:
            ip = d.get("ip_str", "-")
            port = d.get("port", "-")
            banner = d.get("data", "No banner")
            risk_description = assess_risk_with_gpt(banner)
            risk_level = classify_risk_level(risk_description)
            rows.append({
                "IP": ip,
                "Port": port,
                "Risk Level": risk_level,
                "Risk Analysis": risk_description
            })

        df = pd.DataFrame(rows)
        st.success("✅ Scan Complete")
        st.dataframe(df, use_container_width=True, height=500)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Results as CSV", data=csv, file_name="risk_report.csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
