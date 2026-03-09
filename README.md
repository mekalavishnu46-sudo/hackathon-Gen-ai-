🎓 CurricuForge AI
CurricuForge AI is an AI-powered curriculum generator that creates structured learning roadmaps based on a user's skill and learning goal.

The application uses:

Python

Streamlit (UI)

Groq API

LLaMA 3.1 model

It generates:

📚 Learning roadmap

📅 Weekly learning plan

🧠 Learning stages (Beginner → Advanced)

📊 Structured tables

🔁 Learning flow diagrams

🧪 Practice exercises

🚀 Final project ideas

🔗 Useful learning resources

🚀 Features
AI-generated structured curriculum

Clean Markdown formatted output

Weekly roadmap table

Learning flow visualization

Beginner-friendly roadmap

Interactive Streamlit UI

🛠️ Tech Stack
Technology	Purpose
Python	Backend logic
Streamlit	Web interface
Groq API	AI inference
LLaMA 3.1	Language model
📦 Project Structure
CurricuForge-AI
│
├── ai.py
├── requirements.txt
└── README.md
⚙️ Installation Guide
1️⃣ Install Python
Download and install Python

https://www.python.org/downloads/

Verify installation:

python --version
2️⃣ Install Git (Optional but recommended)
Download Git:

https://git-scm.com/downloads

Verify installation:

git --version
3️⃣ Clone the Repository
git clone https://github.com/yourusername/curricuforge-ai.git
cd curricuforge-ai
Or download ZIP and open the folder in VS Code.

4️⃣ Create Virtual Environment
Inside the project folder:

python -m venv .venv
Activate it:

Windows
.venv\Scripts\activate
Mac/Linux
source .venv/bin/activate
5️⃣ Install Required Libraries
Create a requirements.txt

streamlit
groq
Then install dependencies:

pip install -r requirements.txt
🔑 Groq API Setup
Create an API key from the Groq Console:

👉 https://console.groq.com

Steps:

Sign in

Go to API Keys

Click Create API Key

Copy the key

Example:

gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
🔐 Secure API Key (Recommended)
Instead of hardcoding the key, use environment variables.

Windows (PowerShell)
setx GROQ_API_KEY "your_api_key_here"
Mac/Linux
export GROQ_API_KEY="your_api_key_here"
Then modify the code:

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
▶️ Running the Application
Inside the project folder run:

streamlit run ai.py
Streamlit will start a local server.

Example output:

Local URL: http://localhost:8501
Open it in your browser.

🧠 How It Works
User enters:

Skill
Learning Goal
Example:

Skill: Python
Goal: Become job ready in 3 months
The application sends a prompt to Groq AI

The model generates:

Overview

Weekly roadmap

Learning stages

Flow diagram

Exercises

Final project

Resources

The result is displayed using Markdown formatting.

📊 Example Output
Weekly Roadmap
Week	Topics	Practice	Outcome
1	Python Basics	Variables & Loops	Understand syntax
2	Functions	Write mini programs	Code modularity
3	OOP	Classes & Objects	Build reusable code
Learning Flow
Start
 ↓
Basics
 ↓
Practice
 ↓
Projects
 ↓
Mastery
💻 Running in VS Code
Open VS Code

Open the project folder

Open terminal

Run:

.venv\Scripts\activate
pip install -r requirements.txt
streamlit run ai.py
🌟 Future Improvements
Interactive learning graphs

Download curriculum as PDF

Visual roadmap charts

Course resource recommendations

Progress tracking

🤝 Contributing
Contributions are welcome.

Steps:

fork → modify → pull request
📄 License
MIT License

👨‍💻 Author
Vishnu

.gitignore
requirements.txt
README.md
