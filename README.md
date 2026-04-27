# Fair-Hire-AI
FairHire AI is an unbiased resume selection system that evaluates candidates based on experience, education, skills, projects, and certifications using NLP and ML (TF-IDF + Logistic Regression). It ensures fair, merit-based hiring by ignoring sensitive attributes like gender or caste.
# ⚖️ FairHire AI – Unbiased Resume Selection System

## 📌 Overview

FairHire AI is an AI-powered system that ensures **fair and unbiased candidate selection** based purely on merit. It evaluates resumes using **experience, education, skills, projects, and certifications**, while ignoring sensitive attributes like **gender, caste, or name**.

---

## 🎯 Features

* 📄 Resume parsing (TXT/PDF)
* 🤖 ML-based resume classification (TF-IDF + Logistic Regression)
* ⚖️ Fair candidate comparison system
* 📊 Score-based ranking (experience, skills, education, etc.)
* 🚫 Bias-free decision making
* 🖥️ Interactive Streamlit UI

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* PyPDF2
* Regex (NLP preprocessing)

---

## ⚙️ How It Works

1. Upload two resumes
2. System extracts features:

   * Experience
   * Education
   * Skills
   * Projects
   * Certifications
3. Computes a fair score
4. Compares both candidates
5. Selects the best candidate based on merit

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/your-username/fairhire-ai.git
cd fairhire-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run App

```bash
streamlit run app1.py
```

---

## 📂 Project Structure

```
fairhire-ai/
│
├── app1.py              # Streamlit UI
├── compare.py           # Comparison logic
├── train_model.py       # ML training script
├── tfidf.pkl            # TF-IDF vectorizer
├── UpdatedResumeDataSet.csv
└── README.md
```

---

## 📊 Results

* Improved fairness in hiring decisions
* Transparent scoring system
* Merit-based candidate selection

---

## 🎤 Project Objective

To build an AI system that ensures **ethical and unbiased hiring decisions** using machine learning and fairness-aware design.

---

## 🔮 Future Enhancements

* 🤖 Transformer-based NLP (BERT)
* 📊 Fairness visualization dashboard
* 🌐 API + backend integration
* 📱 Android app with Gemini AI
* 🧠 Explainable AI (XAI)

---

## 👨‍💻 Author

Tanmaya Tripathy

---

## 📜 License

This project is for academic and educational purposes.
