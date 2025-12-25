# 📈 Sentix AI: Multilingual Sentiment Intelligence

**Sentix AI** is a professional-grade sentiment analysis tool that leverages State-of-the-Art (SOTA) NLP models to detect emotional tone in 20+ languages. Designed for both individual text analysis and high-volume CSV processing, Sentix AI provides actionable data visualizations for researchers and marketers.

## 🚀 Key Features
- **Global Reach:** Supports English, Spanish, French, Hindi, and more via a multilingual RoBERTa-based transformer.
- **Bulk Processing:** Upload CSV datasets and receive instant sentiment mapping.
- **Visual Analytics:** Interactive Pie and Bar charts for sentiment distribution using Plotly.
- **High Accuracy:** Detects 5 levels of sentiment (from Very Negative to Very Positive) with confidence scores.
- **One-Click Export:** Download processed results as a clean CSV for further reporting.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI/ML:** Hugging Face Transformers, PyTorch, RoBERTa
- **Frontend:** Streamlit
- **Data:** Pandas, Plotly (Visualizations)

## 📦 Installation & Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/mansiggit/sentiment-pro.git](https://github.com/mansiggit/sentix-ai.git)
   cd sentix-ai
2. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Run the App:**
   ```bash
   streamlit run app.py
