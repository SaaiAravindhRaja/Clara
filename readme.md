🧠 AI Calendar Agent — Google Calendar Management with Orgo + OpenAI + Anthropic

This project integrates Orgo, OpenAI, and Anthropic to create an autonomous agent that can manage your Google Calendar through natural language prompts. It uses Orgo’s virtual desktop infrastructure, Agent S2 for GUI automation, and large language models for reasoning and control.

⸻

🚀 Features
	•	✅ Create, edit, or delete calendar events using natural language
	•	🗓️ View and search for existing meetings or appointments
	•	🧭 Navigate Google Calendar in a Chrome browser GUI
	•	🔄 Switch between OpenAI (GPT-4o) or Anthropic (Claude) as the control model
	•	🖥️ Works in Orgo cloud VMs or your local machine

⸻

📦 Tech Stack

Component	Description
Orgo	GUI environment and action execution
Agent S2	Looping agent framework (perception → LLM → act)
OpenAI API	GPT-4o reasoning and planning
Anthropic API	Claude as an alternative controller model
Google Calendar	Controlled via Chrome in a GUI environment


⸻

🔧 Setup

1. Clone the Repo

git clone https://github.com/your-org/ai-calendar-agent.git
cd ai-calendar-agent

2. Set Up Environment

Install VSCode extension to use .ipynb
Open Anaconda Prompt and set current directory to this repo:

conda env create -f orgo-env.yml
conda activate orgo-env

In VSCode, select the orgo-env kernel in your Jupyter notebook.

Alternatively, run .py files via Anaconda Prompt like standard Python scripts.

⸻

3. Configure API Keys

Edit your .env file:

ORGO_API_KEY=your_orgo_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
BROWSER_EXECUTABLE_PATH=/path/to/chrome


⸻

4. Launch Agent

python run_agent.py

The agent will:
	•	Launch an Orgo virtual or local desktop
	•	Open Chrome to Google Calendar
	•	Accept your natural language prompt
	•	Perform the calendar task autonomously

⸻

🗣️ Example Prompts

"Create a meeting tomorrow at 3pm with Sarah about Q3 planning."
"Find my next event with John."
"Reschedule my 10am call to Friday."
"Cancel the 'Yoga' event on Saturday."


⸻

🛠️ Agent Behavior

Agent S2 runs in a loop:
	1.	Capture screen
	2.	LLM interprets via screenshot and current context
	3.	Generate next GUI action
	4.	Orgo API executes mouse/keyboard commands
	5.	Repeat until done

⸻

⚙️ Configuration

Modify config.yaml:

model: openai  # or 'anthropic'
max_steps: 30
temperature: 0.7
browser: chrome
calendar_url: "https://calendar.google.com"


⸻

📁 File Structure

.
├── run_agent.py         # Main loop for launching and controlling the agent
├── actions/             # Mouse/keyboard control logic
├── prompts/             # Prompt engineering templates
├── config.yaml          # Configuration file
├── .env                 # API keys and local paths
├── requirements.txt     # Python dependencies
└── README.md            # This file


⸻

📌 Notes
	•	Make sure you’re signed into Google Calendar for automation to work
	•	Keep your API keys secure — do not hardcode them
	•	Easily switch between OpenAI and Anthropic via config.yaml or .env

⸻

📎 References
	•	Orgo Docs
	•	OpenAI Platform
	•	Anthropic Console
	•	Agent S2 Setup Guide

⸻

🤝 Contributions

Pull requests welcome! For major changes, open an issue to discuss ideas.

⸻

👥 Team

Built by:
@nibess1
@weisintai
@darriusnjh
@SaaiAravindhRaja

⸻
