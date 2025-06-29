# 🔍 ShodanGPT: AI-Augmented Threat Intelligence from the Internet

> Discover, analyze, and understand exposed devices online using Shodan + GPT-4

---

## 📌 Overview

**ShodanGPT** combines the power of [Shodan.io](https://www.shodan.io/) — the search engine for Internet-connected devices — with **OpenAI’s GPT-4** to automatically:

- Search for exposed services and devices online  
- Interpret risk levels from banners and metadata  
- Explain vulnerabilities in natural language  
- Recommend mitigation strategies for security teams  

This project bridges the gap between **raw OSINT data** and **actionable threat intelligence** — ideal for cybersecurity analysts, AI security researchers, and red teams.

---

## 💡 Features

- ✅ Query Shodan programmatically with Python
- ✅ Analyze responses using GPT-4 or GPT-3.5
- ✅ Generate natural-language security assessments
- ✅ Output structured logs (JSON/CSV)
- ✅ (Optional) Visualize and interact via Streamlit UI

---

## 📂 Project Structure



## Project Structure
![image](https://github.com/user-attachments/assets/9d54a8b0-5a9c-4c9c-83ff-e42b53339188)

---

## ⚙️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/shodan-gpt-analyzer.git
cd shodan-gpt-analyzer
```


2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure API keys**

In config.py, add your Shodan and OpenAI keys:

```bash
OPENAI_KEY = "your-openai-key"
SHODAN_KEY = "your-shodan-key"
MODEL = "gpt-4"  # or "gpt-3.5-turbo"
```


## 🚀 Usage

A. **CLI Mode**

```bash
python app.py --query "port:21 Anonymous" --output results/report.csv
```

B. **Streamlit Dashboard (Optional)**

```bash
streamlit run src/dashboard.py
```


## 🔒 Use Cases
- AI-assisted threat reconnaissance
- Red team & pentest prep automation
- SOC analyst tooling augmentation
- GenAI for OSINT and security research

## 🛡️ Disclaimer
This tool is intended for educational and ethical use only. Do not use it to scan or analyze unauthorized systems. The developer is not responsible for misuse.
