Student AI Chatbot 🎓🤖

A modern AI-powered student chatbot built with a secure authentication system, real-time AI responses, and a clean responsive interface. Users can create accounts, log in securely, and interact with an intelligent chatbot powered by LLM APIs.

🚀 Features
🔐 User Authentication System
User Registration
Secure Login & Logout
Session Management
🤖 AI Chatbot
Real-time AI-generated responses
Conversational interface
Chat history support
🗄️ Database Integration
PostgreSQL / NeonDB support
User data & chat storage
🌐 Deployment Ready
Optimized for Vercel deployment
Environment variable support
🎨 Modern UI
Responsive design
Tailwind CSS styling
Clean chat interface
🛠️ Tech Stack
Technology	Usage
HTML/CSS	Frontend Structure
Tailwind CSS	UI Styling
Django	Backend Framework
Django REST Framework	APIs
PostgreSQL / NeonDB	Database
Groq API	AI Response Generation
Vercel	Deployment
📸 Project Preview

Add screenshots of your chatbot UI here

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-chatbot.git
cd student-chatbot
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your_secret_key
DEBUG=True

DATABASE_URL=your_database_url

GROQ_API_KEY=your_groq_api_key
5️⃣ Run Migrations
python manage.py migrate
6️⃣ Start Development Server
python manage.py runserver
🌍 Live Demo

🔗 Your deployed project link here

Example:

https://your-project.vercel.app
📂 Project Structure
student-chatbot/
│
├── accounts/
├── chatbot/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── vercel.json
└── README.md
🔒 Authentication Flow
User creates an account
Credentials are securely stored
User logs in
Session authentication grants chatbot access
📌 Future Improvements
Chat history persistence
Voice input support
Dark mode
Multiple AI model support
File upload & PDF analysis
👨‍💻 Developer

Muhammad Abdullah

💼 LinkedIn
🌐 Portfolio
📧 Contact
