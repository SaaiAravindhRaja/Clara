# 🧠 AI Calendar Agent — Google Calendar Management with Orgo + OpenAI + Anthropic

This project integrates [Orgo](https://www.orgo.ai/), [OpenAI](https://openai.com/), and [Anthropic](https://www.anthropic.com/) to create an autonomous agent that can manage your **Google Calendar** through natural language prompts. It uses Orgo’s virtual desktop infrastructure, Agent S2 for GUI automation, and large language models for reasoning and control.

---

## 🚀 Features

- ✅ Create, edit, or delete calendar events using natural language
- 🗓️ View and search for existing meetings or appointments
- 🧭 Navigate Google Calendar in a Chrome browser GUI
- 🔄 Switch between OpenAI (GPT-4o) or Anthropic (Claude) as the control model
- 🖥️ Works in Orgo cloud VMs or your local machine

---

## 📦 Tech Stack

| Component       | Description                                      |
|----------------|--------------------------------------------------|
| **Orgo**        | GUI environment and action execution             |
| **Agent S2**    | Looping agent framework (perception → LLM → act) |
| **OpenAI API**  | GPT-4o reasoning and planning                    |
| **Anthropic API** | Claude as an alternative controller model     |
| **Google Calendar (web)** | Controlled via Chrome in a GUI environment |

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-org/ai-calendar-agent.git
cd ai-calendar-agent
````

### 2. Set Up Environment

install vscode extension to use ipynb
Open anaconda prompt and make your current directy that of this repository
```bash
conda env create -f orgo-env.yml
conda activate orgo-env
```
Select python kernel of the ipynb to be orgo-env

### 3. Configure API Keys

Edit `.env` with your credentials:

```env
ORGO_API_KEY=your_orgo_key
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
BROWSER_EXECUTABLE_PATH=/path/to/chrome
```

### 4. Launch Agent

```bash
python run_agent.py
```

The agent will:

* Launch an Orgo virtual desktop (or local desktop)
* Open Chrome and navigate to [Google Calendar](https://calendar.google.com)
* Accept your natural language prompt
* Perform calendar tasks accordingly

---

## 🗣️ Example Prompts

```text
"Create a meeting tomorrow at 3pm with Sarah about Q3 planning."
"Find my next event with John."
"Reschedule my 10am call to Friday."
"Cancel the 'Yoga' event on Saturday."
```

---

## 🛠️ Agent Behavior

Agent S2 follows a loop:

1. Takes a screenshot of the screen
2. Sends it to the selected LLM (OpenAI or Anthropic)
3. LLM determines next GUI action
4. Executes mouse/keyboard commands via Orgo API
5. Repeats until task is completed

---

## ⚙️ Configuration

You can tweak behavior in `config.yaml`:

```yaml
model: openai  # or 'anthropic'
max_steps: 30
temperature: 0.7
browser: chrome
calendar_url: "https://calendar.google.com"
```

---

## 📁 File Structure

```
.
├── run_agent.py         # Main loop for launching and controlling the agent
├── actions/             # Mouse/keyboard control logic
├── prompts/             # Prompt engineering templates
├── config.yaml          # Configuration file
├── .env                 # API keys and local paths
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 📌 Notes

* You must be signed into Google Calendar in the browser for automation to work.
* Security: Keep your API keys safe. Do **not** hardcode them.
* You can switch between OpenAI and Anthropic via config or `.env`.

---

## 📎 References

* [Orgo Docs](https://docs.orgo.ai/)
* [OpenAI Platform](https://platform.openai.com/)
* [Anthropic Console](https://console.anthropic.com/)
* [Agent S2 Setup Guide](https://www.orgo.ai/blog/simular-agent-s2-setup-orgo)

---

## 🤝 Contributions

Pull requests are welcome! For major changes, open an issue first to discuss your idea.
