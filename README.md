# 🍽️ Restaurant Idea Generator

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39-orange?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-v0.3-purple?style=for-the-badge)


<img width="1910" height="1077" alt="Screenshot (203)" src="https://github.com/user-attachments/assets/bf095116-4e12-413e-9250-12ab1f5259bb" />


---

## 🏷️ Overview

**Restaurant Idea Generator** is a web application built with **Streamlit** and **LangChain** that helps you generate creative restaurant names and menu items based on your selected cuisine.  

The app uses **Google Gemini LLM** to generate unique and fancy restaurant names along with an attractive menu.

---

## 🎨 Features

- Select a **cuisine** from a variety of options:
  - Bangladeshi, Indian, Pakistani, American, Chinese, French, Mexican  
- Generate a **creative restaurant name** automatically  
- Receive a **list of menu items** tailored to the restaurant name  
- Modern, **responsive Streamlit frontend** with visually appealing cards, emojis, and columns  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core programming language |
| Streamlit | Frontend UI and interactive dashboard |
| LangChain | Orchestration of LLM chains for text generation |
| Google Gemini 2.5 | Language model for generating restaurant names and menu items |
| dotenv | Secure API key and environment variable management |

---

## ⚡ Usage

### 1. Clone the repository

```bash
git clone https://github.com/niloysannyal/Restaurant_Idea_Generator.git
cd Restaurant_Idea_Generator
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create a .env file
Add your **Google Gemini API** credentials in .env:
```aiignore
GOOGLE_API_KEY=your_api_key_here
```
### 4. Run the app
```bash
streamlit run main.py
```
**Open your browser at http://localhost:8501 and start generating restaurant ideas! 🍴**

---

## 🖼️ Screenshots

<img width="1910" height="1077" alt="Screenshot (203)" src="https://github.com/user-attachments/assets/0cb08c15-174a-47f6-bea1-5cf84789d9c2" />

The restaurant name and menu items are displayed in visually appealing cards and two-column layout with emojis.

---

## 💡 How it Works

1. Select a cuisine from the sidebar.
2. Click Generate Ideas.
3. LangChain SequentialChain runs:
    - First, generate a creative restaurant name using LLMChain.
    - Second, generate menu items for that restaurant using another LLMChain.
4. Output is displayed in Streamlit cards and columns.
---

## 📂 File Structure
```
Restaurant_Idea_Generator/
│
├── main.py                  # Streamlit frontend
├── langchain_helper.py      # LLM chains for generating names & menu
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
└── README.md                # Project documentation
```
---

## 🎯 Future Improvements

- Add images for each menu item
- Save generated restaurant ideas to a database or PDF
- Allow users to customize menu item types
- Add multi-language support for cuisines

---

## 💌 Author

**Niloy Sannyal**  
- Email: [niloysannyal@gmail.com](mailto:niloysannyal@gmail.com)  
- GitHub: [https://github.com/niloysannyal](https://github.com/niloysannyal)  

---
