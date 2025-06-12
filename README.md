
# Nyayasarthi 🧑‍⚖️🤖  
**AI-Based Virtual Legal Assistant for the Department of Justice (SIH 2024)**

> “Nyayasarthi” — your digital guide to the corridors of justice.

---

## 🚀 Project Overview

**Nyayasarthi** is an intelligent, interactive AI-powered chatbot developed as a part of **Smart India Hackathon 2024**, built to assist citizens in navigating the **Department of Justice (DoJ), Ministry of Law & Justice, Government of India**.

The virtual assistant aims to:
- Democratize legal information access
- Enhance public interaction with DoJ services
- Provide real-time, dynamic responses using AI/ML

**Problem Statement ID:** 1700  
**Title:** *Developing an AI-based Interactive Chatbot or Virtual Assistant for the Department of Justice Website*

---

## 🎯 Problem Statement Summary

Citizens often struggle to find relevant legal and judicial information across scattered portals. This project addresses that gap by offering a unified chatbot that helps users:
- Learn about various DoJ divisions
- Check judge appointments and vacancies
- Access data from the National Judicial Data Grid (NJDG)
- Get info on traffic fine payments, eFiling, Fast Track Courts
- Track case status
- Download the eCourts app
- Use Tele Law services and much more

> The chatbot is designed to **learn over time**, becoming smarter with interactions and scalable for handling large datasets.

---

## 🧠 Features

> 🧠 This project was originally built using **Jamba 1.5 Large** by AI21 Labs. Since then, AI21 has released **Jamba 1.6 Large** with improvements in performance and API capabilities. During development, Jamba API was completely free to use — now it includes pricing tiers. Plan your integration accordingly.

- 🔍 **Natural Language Understanding (NLU)**  
  Handles diverse queries using LLM-backed understanding.

- 🗺️ **Contextual Q&A**  
  Smart info delivery about judiciary structure, pending cases, court services.

- 🌐 **Web Scraping Module**  
  Pulls live data from [doj.gov.in](https://doj.gov.in) to ensure up-to-date responses.

- 📈 **Scalable Architecture**  
  Designed for future expansion and large data handling.

- 🛠️ **Extensible Modules**  
  Easy to integrate additional data sources like NJDG, eCourts, Tele-Law APIs.

---

## 🏗️ Tech Stack

| Layer              | Tech Used                            |
|-------------------|---------------------------------------|
| Frontend          | HTML, CSS, JavaScript (optionally React) |
| Backend           | Python (Flask/FastAPI)                |
| NLP Engine        | OpenAI GPT / Transformers / Rasa      |
| Web Scraping      | BeautifulSoup, Requests               |
| Database (optional)| SQLite / MongoDB / Firebase          |
| Deployment        | Render / Heroku / GitHub Pages (demo) |

---

## 📂 Project Structure

```bash
Nyayasarthi/
├── static/              # Frontend assets
├── templates/           # HTML pages
├── scraper/             # DOJ web scraper module
├── chatbot/             # Core chatbot logic
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md            # You’re here!
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Joydeep2005Banik/Nyayasarthi.git
cd Nyayasarthi
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
python main.py
```

---

## 📚 Dataset & References

- 🔗 **Dataset / Source**: [https://doj.gov.in](https://doj.gov.in)
- 🧠 Powered by OpenAI / Custom NLP models
- 🕸️ Web scraping handled via BeautifulSoup

---

## 👥 Contributors

Built with passion by our team of 6 for SIH 2024:

- Joydeep Banik  
- Sk. Sumit Ahmed  
- Priyanka Pal  
- Rupayan Biswas  
- Mainak Bal  
- Priti Kumari Mahato

---


## 🙌 Acknowledgements

Thanks to:
- **Smart India Hackathon**
- **Department of Justice**
- Our mentors, faculty, and sleepless caffeine-filled nights

---

## 💡 Future Scope

- Voice assistant support (in multiple Indian languages)
- Integration with real-time NJDG and eCourt APIs
- User authentication + personalized legal help
- Analytics dashboard for DoJ usage metrics

---

## 📫 Contact

For queries, suggestions, or just to say hi:

📧 Joydeep Banik – [LinkedIn](https://www.linkedin.com/in/joydeepbanik/)  
📦 GitHub – [@Joydeep2005Banik](https://github.com/Joydeep2005Banik)

---

> _“Nyayasarthi — because justice shouldn't require a law degree to understand.”_
