🤖 AI Agent Assistant
🧩 Overview

This project is an AI Agent Assistant built using LangChain, LangGraph, and the OpenAI API.
It acts as an intelligent chatbot capable of understanding user queries and executing specific tasks using custom tools — from performing calculations to telling jokes and fetching dictionary meanings.

It combines the power of LLMs with real-world functionality through Python-defined tools.

⚙️ Features

✅ Conversational Agent – Chat naturally with an AI assistant
🧮 Calculator Tools – Perform addition, subtraction, multiplication, and division
💬 Greeting Tool – Greets users in a friendly way
😂 Joke Tool – Tells fun programming or general jokes
📖 Dictionary Tool – Fetches real-time word meanings using an API
💪 Motivation Tool – Gives short motivational quotes
⚡ Streaming Responses – See answers appear word by word for an interactive chat feel

🧰 Tech Stack

Python 3.10+

LangChain – Agent and tool management

LangGraph – Prebuilt agent execution framework

OpenAI API – Natural language understanding

python-dotenv – Secure environment variable handling

Requests – For external API integration

📁 Project Structure
Project_1/
│
├── my_tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── greet.py
│   ├── fun.py
│   ├── dictionary.py
│
├── main.py
├── .env
├── requirements.txt
└── README.md

🔐 Environment Variables

You must have an OpenAI API key stored securely in a .env file:

OPENAI_API_KEY=your_openai_api_key_here


⚠️ Never push your .env file to GitHub.
Add .env to your .gitignore.

🧩 Installation & Setup

Clone the Repository

git clone https://github.com/PallaviSatram/AI_Agent_Assistant.git
cd Project_1


Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate  # On Windows


Install Dependencies

pip install -r requirements.txt


Add Your OpenAI API Key

Create a .env file in the root folder

Paste your API key as shown above

Run the Application

python main.py

💬 Example Usage
Welcome! I'm your AI assistant. Type 'quit' to exit.
You can ask me to perform calculations or chat with me.

You: add 10 and 5  
Assistant: The result of 10 + 5 is 15.

You: tell me a joke  
Assistant: Why do Python programmers prefer dark mode? Because light attracts bugs 🐛

You: meaning of "synergy"  
Assistant: Synergy → The combined effect greater than the sum of individual parts.

You: motivate me  
Assistant: You don’t need to be the best today — just better than yesterday.

💡 Future Enhancements

🌤 Add a Weather Tool (via OpenWeather API)
📰 Add a News Fetcher Tool
💱 Integrate Currency Converter Tool
📊 Add a File Save/Report Generator Tool

👩‍💻 Author
Pallavi Satram

