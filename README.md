<h1 align="center">🎓 Student AI Chatbot</h1>

<p align="center">
  An AI-powered student assistant with secure authentication, intelligent conversations, and a modern responsive interface.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django" />
  <img src="https://img.shields.io/badge/TailwindCSS-Frontend-blue?style=for-the-badge&logo=tailwindcss" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql" />
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel" />
</p>

---

## 🚀 About The Project

Student AI Chatbot is a full-stack AI web application designed to help students interact with an intelligent chatbot through a secure and user-friendly platform.

The project includes:

- 🔐 User Authentication System
- 🤖 AI Chat Functionality
- 💬 Interactive Chat Interface
- 🗄️ PostgreSQL Database Integration
- ☁️ Vercel Deployment Support
- 🎨 Responsive Modern UI

---

# ✨ Features

## 🔑 Authentication System

- User Registration
- Secure Login & Logout
- Session-Based Authentication
- Protected Routes

## 🤖 AI Chatbot

- Real-time AI Responses
- Intelligent Conversation Flow
- Clean Chat UI
- API Integration with Groq LLM

## 🎨 Frontend

- Responsive Design
- Tailwind CSS Styling
- Modern User Experience
- Mobile Friendly Interface

## ⚙️ Backend

- Django Framework
- Django REST Framework APIs
- PostgreSQL / NeonDB Support
- Environment Variable Configuration

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Django | Backend Framework |
| Django REST Framework | API Development |
| Tailwind CSS | Frontend Styling |
| HTML/CSS | Frontend Structure |
| PostgreSQL / NeonDB | Database |
| Groq API | AI Model Integration |
| Vercel | Deployment Platform |

---

# 📂 Project Structure

```bash
student-chatbot/
│
├── accounts/          # Authentication System
├── chatbot/           # Chatbot Logic
├── templates/         # HTML Templates
├── static/            # Static Files
├── manage.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/student-chatbot.git

cd student-chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `.env` File

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

GROQ_API_KEY=your_groq_api_key
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

---

# 🌐 Live Demo

🔗 https://your-project.vercel.app

---

# 🔒 Authentication Flow

```text
User Registration
        ↓
Secure Credential Storage
        ↓
User Login
        ↓
Authenticated Session
        ↓
Access AI Chatbot
```

---

# 📸 Screenshots

## 🔐 Login Page

Add Screenshot Here

---

## 🤖 Chat Interface

Add Screenshot Here

---

# 🚀 Future Improvements

- Chat History Storage
- Voice Input Support
- Dark Mode
- File Upload Support
- Multi-Model AI Support
- Real-Time Streaming Responses

---

# 👨‍💻 Developer

## Muhammad Abdullah

<p align="left">
  <a href="https://linkedin.com/in/your-linkedin">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" />
  </a>
  
  <a href="https://github.com/your-github">
    <img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" />
  </a>
</p>

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub and share it with others.

---

<p align="center">
  Made with ❤️ using Django & AI
</p>
