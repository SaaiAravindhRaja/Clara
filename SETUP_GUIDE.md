# 🚀 Setup Guide for AI Calendar Agent

## What This Project Does

This is an AI agent that can manage your Google Calendar through natural language commands. It uses:
- **Orgo** for cloud-based GUI automation
- **OpenAI/Anthropic** for AI reasoning
- **Agent S2** for the automation loop (screenshot → LLM → action)

## 🔧 Step-by-Step Setup for Your System

### 1. Environment Setup

Since you're on macOS (darwin), you'll need to set up the environment:

```bash
# Navigate to your project directory
cd /Users/saaiaravindhraja/Desktop/ThisMac/LocalGitHub/Clara

# Create conda environment from the provided file
conda env create -f orgo-env.yml

# Activate the environment
conda activate orgo-env
```

### 2. API Keys Setup

Create a `.env` file in your project root:

```bash
# Create .env file
touch .env
```

Add your API keys to `.env`:

```env
ORGO_API_KEY=your_orgo_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
BROWSER_EXECUTABLE_PATH=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```

### 3. Get Your API Keys

**Orgo API Key:**
1. Go to [Orgo.ai](https://www.orgo.ai/)
2. Sign up/login
3. Get your API key from the dashboard

**OpenAI API Key:**
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create account/login
3. Get API key from API Keys section

**Anthropic API Key:**
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Create account/login
3. Get API key from API Keys section

### 4. Fix Project Configuration

The project ID in your notebook doesn't match your Orgo project. Use the corrected notebook:

```bash
# Use the fixed notebook instead
# src_fixed.ipynb has the correct project ID
```

### 5. Test the Setup

1. Open Jupyter Lab or VS Code with Jupyter extension
2. Open `src_fixed.ipynb`
3. Make sure the kernel is set to `orgo-env`
4. Run the first cell to test the connection

## 🎯 Performance Improvements

### 1. **Optimize LLM Usage**
- Use GPT-4o-mini for faster responses
- Implement caching for repeated tasks
- Batch similar calendar operations

### 2. **Reduce Screenshot Frequency**
- Only take screenshots when UI changes
- Implement smart waiting instead of constant polling
- Use element detection instead of full screenshots

### 3. **Improve Error Handling**
- Add retry logic for failed operations
- Implement fallback strategies
- Better logging for debugging

### 4. **Optimize Browser Automation**
- Use headless mode when possible
- Implement smart element selection
- Reduce unnecessary page loads

## 🐛 Common Issues & Solutions

### Issue: "Project ID not found"
**Solution:** Make sure you're using the correct project ID from `.orgo/project.json`

### Issue: "API key invalid"
**Solution:** Check your `.env` file and ensure API keys are correct

### Issue: "Chrome not found"
**Solution:** Update `BROWSER_EXECUTABLE_PATH` in `.env` for macOS:
```env
BROWSER_EXECUTABLE_PATH=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```

### Issue: "Environment not found"
**Solution:** Make sure you've activated the conda environment:
```bash
conda activate orgo-env
```

## 📝 Usage Examples

Once set up, you can use natural language commands like:

```python
# Create events
computer.prompt("Create a meeting tomorrow at 3pm with Sarah about Q3 planning")

# Find events
computer.prompt("Find my next event with John")

# Reschedule events
computer.prompt("Reschedule my 10am call to Friday")

# Cancel events
computer.prompt("Cancel the 'Yoga' event on Saturday")
```

## 🔍 Troubleshooting

1. **Check Orgo Status:** Make sure your Orgo project is active
2. **Verify API Keys:** Test each API key individually
3. **Check Environment:** Ensure all dependencies are installed
4. **Monitor Logs:** Look for error messages in the notebook output

## 🚀 Next Steps

1. Test with simple calendar operations
2. Gradually increase complexity
3. Monitor performance and optimize
4. Add custom prompts for your specific use cases

Need help? Check the [Orgo documentation](https://docs.orgo.ai/) or create an issue in the repository. 