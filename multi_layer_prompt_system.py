"""
Multi-Layer LLM System for Calendar Event Creation
Layer 1: Prompt Engineering LLM - Refines user input and gathers missing details
Layer 2: Agent-S - Executes the refined prompt via GUI automation
"""

import os
import json
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import openai
from dotenv import load_dotenv
from agent_s_interface import create_calendar_event_with_agent_s

# Load environment variables from .env file
load_dotenv()

class PromptEngineeringLayer:
    """
    Layer 1: Handles prompt refinement and detail gathering
    """
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history = []
        
    def analyze_user_input(self, user_input: str) -> Dict:
        """
        Analyzes user input to extract event details and identify missing information
        """
        system_prompt = """You are a calendar event analyzer. Your job is to:
1. Extract any event details from user input
2. Identify what information is missing for a complete calendar event
3. Return a structured response

IMPORTANT DATE/TIME PARSING RULES:
- Current date is January 28, 2025 (use this as reference for relative dates)
- "August 22nd" = "2025-08-22" (always use 2025 for future dates)
- "8am" = "08:00", "2pm" = "14:00", "8:30am" = "08:30"
- "tomorrow" = January 29, 2025 = "2025-01-29"
- "next Friday" = calculate the next Friday from January 28, 2025

Required fields for a calendar event:
- title: Event name/description
- date: Specific date (YYYY-MM-DD format, use 2025 for future dates)
- time: Start time (HH:MM format, 24-hour)
- duration: How long the event lasts (e.g., "1 hour", "2 hours", "30 minutes")
- location: Where the event takes place (optional)

Return your analysis as JSON with:
- "extracted_details": {dict of found information with correct date/time formatting}
- "missing_details": [list of missing required fields]
- "confidence": float between 0-1 for how complete the information is
- "clarification_questions": [list of specific questions to ask user]

EXAMPLES:
- "diving event August 22nd 8am" → date: "2025-08-22", time: "08:00"
- "meeting tomorrow at 2pm" → date: "2025-01-29", time: "14:00"
- "gym session at 8:30am" → time: "08:30"
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analyze this calendar request: {user_input}"}
                ],
                temperature=0.3
            )
            
            # Parse the JSON response
            analysis = json.loads(response.choices[0].message.content)
            return analysis
            
        except Exception as e:
            print(f"Error analyzing user input: {e}")
            return {
                "extracted_details": {},
                "missing_details": ["title", "date", "time", "duration"],
                "confidence": 0.0,
                "clarification_questions": ["Could you provide more details about your calendar event?"]
            }
    
    def ask_clarification_questions(self, questions: List[str]) -> Dict[str, str]:
        """
        Interactively asks user for missing information
        """
        answers = {}
        print("\nI need some additional details to create your calendar event:")
        
        for question in questions:
            answer = input(f"{question} ")
            if answer.strip():
                answers[question] = answer.strip()
        
        return answers
    
    def refine_event_details(self, initial_details: Dict, user_answers: Dict[str, str]) -> Dict:
        """
        Uses LLM to combine initial details with user answers into complete event info
        """
        system_prompt = """You are a calendar event detail refiner. Take the initial extracted details and user answers to create a complete event specification.

Return a JSON object with these exact fields:
- "title": string
- "date": string in YYYY-MM-DD format
- "time": string in HH:MM format (24-hour)
- "duration": string like "1 hour", "30 minutes", "2 hours"
- "location": string (can be empty if not provided)

Be smart about parsing dates and times. Convert relative dates like "tomorrow", "next Friday" to actual dates.
Convert times like "8am", "2:30 PM" to 24-hour format.
"""

        prompt = f"""
Initial extracted details: {json.dumps(initial_details)}
User answers to clarification questions: {json.dumps(user_answers)}

Please create a complete event specification.
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            
            refined_details = json.loads(response.choices[0].message.content)
            return refined_details
            
        except Exception as e:
            print(f"Error refining event details: {e}")
            return initial_details
    
    def generate_agent_s_instruction(self, event_details: Dict) -> str:
        """
        Generates optimized instruction for Agent-S based on complete event details
        """
        system_prompt = """You are an expert at creating precise instructions for GUI automation agents. 
Create a detailed, step-by-step instruction for Agent-S to create a calendar event in Google Calendar via Firefox.

CRITICAL: Pay special attention to date and time formatting:
- Date format: If date is "2025-08-22", enter it as "August 22, 2025" or "08/22/2025"
- Time format: If time is "08:00", enter it as "8:00 AM" or "08:00"
- Duration: If duration is "2 hours", set end time accordingly (e.g., 8:00 AM to 10:00 AM)

The instruction should be:
1. Specific and actionable
2. Include all necessary details with correct date/time formatting
3. Handle potential UI variations
4. Include confirmation steps

Format: Clear, sequential steps that a GUI automation agent can follow.
"""

        prompt = f"""
Create an Agent-S instruction to create this calendar event:
{json.dumps(event_details, indent=2)}

IMPORTANT: Make sure to format the date and time correctly for Google Calendar:
- Convert date from YYYY-MM-DD to a human-readable format
- Convert time from 24-hour to 12-hour format if needed
- Calculate end time based on duration

The agent should:
1. Navigate to Google Calendar (assume already open)
2. Click "Create" or "+" button
3. Enter the title: "{event_details.get('title', 'New Event')}"
4. Set the date correctly: {event_details.get('date', 'today')}
5. Set the time correctly: {event_details.get('time', '12:00')}
6. Set duration: {event_details.get('duration', '1 hour')}
7. Add location if provided: {event_details.get('location', '')}
8. Save the event
9. Confirm the event was created successfully
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error generating Agent-S instruction: {e}")
            return f"Create a calendar event titled '{event_details.get('title', 'New Event')}' on {event_details.get('date', 'today')} at {event_details.get('time', '12:00')}."

class MultiLayerCalendarSystem:
    """
    Main system that orchestrates the two-layer approach
    """
    
    def __init__(self, openai_api_key: str):
        self.prompt_engineer = PromptEngineeringLayer(openai_api_key)
        
    def create_calendar_event(self, user_input: str) -> bool:
        """
        Main method that handles the complete flow from user input to event creation
        """
        print(f"🎯 Processing request: {user_input}")
        print("=" * 50)
        
        # Layer 1: Analyze and refine the prompt
        print("🧠 Layer 1: Analyzing your request...")
        analysis = self.prompt_engineer.analyze_user_input(user_input)
        
        print(f"📊 Confidence level: {analysis['confidence']:.1%}")
        print(f"📝 Extracted details: {analysis['extracted_details']}")
        
        # If we need more information, ask for it
        if analysis['confidence'] < 0.8 and analysis['clarification_questions']:
            print(f"❓ Missing information: {analysis['missing_details']}")
            user_answers = self.prompt_engineer.ask_clarification_questions(
                analysis['clarification_questions']
            )
            
            # Refine the details with user answers
            print("🔄 Refining event details...")
            event_details = self.prompt_engineer.refine_event_details(
                analysis['extracted_details'], 
                user_answers
            )
        else:
            event_details = analysis['extracted_details']
        
        print(f"✅ Final event details: {json.dumps(event_details, indent=2)}")
        
        # Generate optimized instruction for Agent-S
        print("🎨 Generating optimized instruction for Agent-S...")
        agent_s_instruction = self.prompt_engineer.generate_agent_s_instruction(event_details)
        
        print(f"🤖 Agent-S Instruction:\n{agent_s_instruction}")
        print("=" * 50)
        
        # Layer 2: Execute with Agent-S
        print("🚀 Layer 2: Executing with Agent-S...")
        try:
            create_calendar_event_with_agent_s(agent_s_instruction)
            print("✅ Calendar event creation completed!")
            return True
        except Exception as e:
            print(f"❌ Error during Agent-S execution: {e}")
            return False

def main():
    """
    Main function to run the multi-layer system
    """
    # Get API key from environment variables
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    
    # Initialize the system
    calendar_system = MultiLayerCalendarSystem(api_key)
    
    print("🎉 Multi-Layer Calendar System Ready!")
    print("🎯 STEP-BY-STEP DEMO:")
    print("=" * 60)
    
    # Demo with your diving example
    demo_input = "create a diving event on August 22nd at 8am"
    print(f"📅 DEMO INPUT: {demo_input}")
    print("-" * 60)
    
    success = calendar_system.create_calendar_event(demo_input)
    
    print("\n" + "=" * 60)
    print("🎊 DEMO COMPLETE!")
    print("\n🔍 WHAT HAPPENED:")
    print("1. Layer 1 (Prompt Engineer) analyzed your input")
    print("2. It identified missing details and asked questions")
    print("3. It generated optimized instructions for Agent-S")
    print("4. Layer 2 (Agent-S) would execute on your Orgo desktop")
    print("\n🌐 Agent-S will control: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("📱 You'll see the automation happen in your Orgo browser window")
    
    return success

if __name__ == "__main__":
    main()