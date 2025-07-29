# 🎯 Multi-Layer LLM Calendar System

## Overview
This system implements a **two-layer LLM approach** for creating calendar events:

1. **Layer 1 (Prompt Engineering LLM)**: Analyzes user input, identifies missing details, asks clarifying questions, and generates optimized prompts
2. **Layer 2 (Agent-S)**: Executes the refined prompt via GUI automation to actually create the calendar event

## Architecture

```
User Input → Layer 1 (Prompt Engineer) → Layer 2 (Agent-S) → Calendar Event
             ↓                           ↓
             Refinement & Questions      GUI Automation
```

## Files

- `multi_layer_prompt_system.py` - Core multi-layer system
- `gui_calendar_system.py` - GUI interface using tkinter
- `test_multi_layer_system.py` - Test script
- `prompt_engineer.py` - Updated with smart method integration

## Usage

### 1. Terminal Interface
```bash
python multi_layer_prompt_system.py
```

### 2. GUI Interface
```bash
python gui_calendar_system.py
```

### 3. Enhanced Prompt Engineer
```bash
python prompt_engineer.py
```

## Example Interactions

**Input**: "Create a diving event on August 22nd at 8am"

**Layer 1 Analysis**:
- Extracts: title="diving event", date="2025-08-22", time="08:00"
- Missing: duration
- Asks: "How long will the diving event last?"

**User Response**: "2 hours"

**Layer 1 Output**: Complete event details + optimized Agent-S instruction

**Layer 2 Execution**: Agent-S creates the actual calendar event

## Key Features

### Smart Analysis
- Extracts event details from natural language
- Identifies missing information
- Asks targeted clarification questions
- Handles relative dates ("tomorrow", "next Friday")
- Converts time formats ("8am" → "08:00")

### Optimized Instructions
- Generates detailed, step-by-step instructions for Agent-S
- Handles UI variations and edge cases
- Includes confirmation steps

### Multiple Interfaces
- Command-line interface for developers
- GUI interface for end users
- Integration with existing prompt_engineer.py

## Configuration

Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Testing

Run the test suite:
```bash
python test_multi_layer_system.py
```

This tests the prompt engineering layer without executing Agent-S.

## Integration with Existing Code

The system integrates seamlessly with your existing:
- `agent_s_interface.py` - For GUI automation
- `performance_optimizer.py` - For performance monitoring
- Orgo infrastructure

## Benefits

1. **Better User Experience**: Natural language input instead of structured forms
2. **Higher Success Rate**: Refined prompts lead to better Agent-S execution
3. **Iterative Refinement**: System asks for missing details automatically
4. **Flexible Interface**: Terminal, GUI, or programmatic access
5. **Backward Compatible**: Works with existing Agent-S setup

## Next Steps

1. Test with your Agent-S setup
2. Customize the prompt templates for your specific use case
3. Add more event types (recurring events, reminders, etc.)
4. Integrate with performance monitoring
5. Add voice input support