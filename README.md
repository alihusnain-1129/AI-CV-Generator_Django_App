# AI CV Generator

AI CV Generator is a web application that uses AI and MCP (Model Context Protocol) tools to generate professional CVs from raw text or existing CV content. The app is built with **Django** for the backend and provides a simple and interactive web interface for users.

---

## Features

- Generate professional CVs in a clean, structured template.
- Uses AI tools (MCP server) for:
  - Summarizing experience
  - Extracting education, skills, and certifications
  - Formatting the CV automatically
- Easy-to-use web interface with a single input form.
- Fully modular: You can replace the MCP model or LLM API easily.

---

## Technologies Used

- **Backend:** Django 5.2
- **AI/LLM:** MCP server + LLM API (Claude Desktop, OpenRouter, etc.)
- **Frontend:** HTML, CSS
- **Python Packages:** Requests, Django, Python-dotenv

---

## Installation

1. **Clone the repository:**

git clone https://github.com/<your-username>/ai-cv-generator.git
cd ai-cv-generator

2. **Create a virtual environment and activate it:**

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. **Install dependencies:**

pip install -r requirements.txt
   
4. **Create .env file and add your LLM API key:**

LLM_API_KEY=your_api_key_here

5. **Run the Django server:**

python manage.py runserver

6. **Open the web app:**

Visit http://127.0.0.1:8000 in your browser.

**Usage**
Paste your CV or experience text into the input form.
Click Generate CV.
View the generated CV in the template format.


**Project Structure**
ai-cv-generator/
├── config/          # Django settings & project configuration
├── core/            # Django app containing views, MCP integration
│   ├── mcp/
│   │   └── main.py  # MCP tool functions
│   └── views.py
├── templates/
│   └── index.html
├── .env             # LLM API key
├── requirements.txt
├── manage.py
└── README.md

**Notes**
Ensure your MCP tool is configured correctly with your chosen LLM API.
Output CV is generated in a single formatted template for easy download or copy.
For large CVs, make sure your LLM usage fits within the token/credit limits.
