# ⚡ Quick Start Guide

## 🚀 Get Running in 5 Minutes

### 1. Run the Setup Script
```bash
./setup.sh
```

### 2. Get Your API Keys
- **Orgo**: https://www.orgo.ai/ → Sign up → Get API key
- **OpenAI**: https://platform.openai.com/ → API Keys → Create new key
- **Anthropic**: https://console.anthropic.com/ → API Keys → Create new key

### 3. Update .env File
```bash
nano .env
```
Replace the placeholder values with your actual API keys.

### 4. Activate Environment & Test
```bash
conda activate orgo-env
python performance_optimizer.py
```

### 5. Use the Agent
```bash
jupyter lab src_fixed.ipynb
```

## 🎯 What This Does

This AI agent can:
- ✅ Create calendar events with natural language
- ✅ Find and search your calendar
- ✅ Reschedule meetings
- ✅ Cancel appointments
- ✅ Navigate Google Calendar automatically

## 💡 Example Commands

```python
# Create events
computer.prompt("Schedule a meeting with John tomorrow at 3pm")

# Find events  
computer.prompt("What's my next meeting?")

# Reschedule
computer.prompt("Move my 2pm meeting to Friday")

# Cancel
computer.prompt("Cancel the yoga class on Saturday")
```

## 🔧 Performance Improvements Added

1. **Caching** - Avoids redundant LLM calls
2. **Retry Logic** - Handles failures gracefully
3. **Batch Operations** - Process multiple tasks efficiently
4. **Smart Screenshots** - Reduces unnecessary screenshots
5. **Performance Metrics** - Monitor and optimize

## 🆘 Need Help?

- Check `SETUP_GUIDE.md` for detailed instructions
- Run `python performance_optimizer.py` to test everything
- Make sure your Orgo project is active
- Verify all API keys are correct in `.env`

## 🚨 Common Issues

**"Project ID not found"** → Use `src_fixed.ipynb` instead of `src.ipynb`
**"API key invalid"** → Check your `.env` file
**"Environment not found"** → Run `conda activate orgo-env`

---

**Ready to automate your calendar! 🗓️✨** 