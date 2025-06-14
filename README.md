# 🤖 Gemini LLM Q&A App

This is a simple Streamlit-based web application that integrates with **Google's Gemini Pro (Flash)** LLM via the `google-generativeai` API. It allows users to interact with the model in a Q&A style chat interface.

## 🚀 Features

- Streamed responses from **Gemini 2.0 Flash**
- Maintains **chat history** between questions
- Clean and intuitive **Streamlit UI**
- Uses **environment variable** for secure API key management

## 📦 Requirements

- Python 3.8+
- Streamlit
- python-dotenv
- google-generativeai

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gemini-qa-app.git
   cd gemini-qa-app
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables**
Create a .env file in the root directory and add your Gemini API key:
    ```bash
    GEMINI_API_KEY=your_google_generative_ai_key

5. **Run the app**

   ```bash
   streamlit run app.py
   
