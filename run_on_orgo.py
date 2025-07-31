#!/usr/bin/env python3
"""
🎯 Run AI Calendar System on Orgo Cloud Desktop
This script runs the complete system on your Orgo virtual desktop
"""

import os
import json
from dotenv import load_dotenv
from orgo import Computer

# Load environment variables
load_dotenv()

def setup_orgo_computer():
    """Setup Orgo computer with your project"""
    orgo_api_key = os.getenv("ORGO_API_KEY")
    if not orgo_api_key:
        print("❌ ORGO_API_KEY not found in .env file")
        return None
    
    # Read project ID from .orgo/project.json if it exists
    project_id = None
    try:
        with open('.orgo/project.json', 'r') as f:
            config = json.load(f)
            project_id = config.get('project_id')
    except FileNotFoundError:
        # Use the project ID from your URL
        project_id = "computer-ppgg5d6j"
    
    print(f"🌐 Connecting to Orgo project: {project_id}")
    
    try:
        computer = Computer(project_id=project_id)
        print("✅ Connected to Orgo successfully!")
        return computer
    except Exception as e:
        print(f"❌ Failed to connect to Orgo: {e}")
        return None

def run_complete_demo_on_orgo():
    """Run a complete demo on Orgo cloud"""
    print("🎯 AI Calendar System - Complete Orgo Demo")
    print("=" * 50)
    
    # Setup Orgo
    computer = setup_orgo_computer()
    if not computer:
        return False
    
    # Import our multi-layer system
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    calendar_system = MultiLayerCalendarSystem(openai_api_key)
    
    # Demo input
    demo_input = "Create a diving event on August 22nd at 8am for 2 hours"
    print(f"📅 Demo Input: {demo_input}")
    print("-" * 50)
    
    # Layer 1: Analyze and refine
    print("🧠 Layer 1: Analyzing input...")
    analysis = calendar_system.prompt_engineer.analyze_user_input(demo_input)
    
    print(f"📊 Analysis Results:")
    print(f"   Confidence: {analysis.get('confidence', 0):.1%}")
    print(f"   Extracted: {analysis.get('extracted_details', {})}")
    print(f"   Missing: {analysis.get('missing_details', [])}")
    
    # Generate Agent-S instruction
    if analysis.get('confidence', 0) >= 0.7:
        print("\n🎨 Generating optimized instruction for Orgo...")
        
        # Create a more specific instruction for Orgo
        event_details = analysis.get('extracted_details', {})
        orgo_instruction = f"""
        Open Firefox browser and navigate to https://calendar.google.com
        
        Create a new calendar event with these details:
        - Title: {event_details.get('title', 'New Event')}
        - Date: {event_details.get('date', 'Today')}
        - Time: {event_details.get('time', '12:00')}
        - Duration: 2 hours
        
        Steps:
        1. Click the "Create" button
        2. Fill in the event title
        3. Set the date and time
        4. Save the event
        5. Confirm it appears on the calendar
        """
        
        print(f"🤖 Orgo Instruction Generated:")
        print(orgo_instruction)
        
        # Layer 2: Execute on Orgo
        print("\n🚀 Layer 2: Executing on Orgo cloud...")
        print("🌐 You can watch the automation at: https://www.orgo.ai/projects/computer-ppgg5d6j")
        
        try:
            result = computer.prompt(orgo_instruction)
            print(f"✅ Orgo Execution Result: {result}")
            return True
        except Exception as e:
            print(f"❌ Orgo execution failed: {e}")
            return False
    else:
        print("❓ Need more information from user")
        return False

def run_interactive_orgo_session():
    """Run interactive session with Orgo"""
    print("🎯 Interactive AI Calendar System on Orgo")
    print("=" * 40)
    
    # Setup
    computer = setup_orgo_computer()
    if not computer:
        return
    
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    openai_api_key = os.getenv("OPENAI_API_KEY")
    calendar_system = MultiLayerCalendarSystem(openai_api_key)
    
    print("🎉 System ready! Type 'quit' to exit")
    print("🌐 Watch automation at: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print()
    
    while True:
        user_input = input("📅 What calendar event would you like to create? ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if user_input.strip():
            try:
                # Layer 1: Analyze
                print("🧠 Analyzing your request...")
                analysis = calendar_system.prompt_engineer.analyze_user_input(user_input)
                
                print(f"📊 Confidence: {analysis.get('confidence', 0):.1%}")
                
                # If we need more info, ask
                if analysis.get('confidence', 0) < 0.8 and analysis.get('clarification_questions'):
                    for question in analysis.get('clarification_questions', []):
                        answer = input(f"❓ {question} ")
                        if answer.strip():
                            # Update the input with the answer
                            user_input += f" {answer}"
                
                # Generate instruction
                event_details = analysis.get('extracted_details', {})
                orgo_instruction = f"""
                Open Firefox and go to https://calendar.google.com
                Create a calendar event:
                - Title: {event_details.get('title', 'New Event')}
                - Date: {event_details.get('date', 'today')}
                - Time: {event_details.get('time', '12:00')}
                Click Create, fill details, and save.
                """
                
                # Layer 2: Execute
                print("🚀 Executing on Orgo...")
                result = computer.prompt(orgo_instruction)
                print(f"✅ Result: {result}")
                print()
                
            except Exception as e:
                print(f"❌ Error: {e}")
                print()

def main():
    """Main function"""
    print("🎯 AI Calendar System - Orgo Edition")
    print("=" * 40)
    
    print("Choose your option:")
    print("1. 🎬 Run Complete Demo")
    print("2. 💬 Interactive Session")
    print("3. ❌ Exit")
    print()
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        success = run_complete_demo_on_orgo()
        if success:
            print("\n🎊 Demo completed successfully!")
        else:
            print("\n😞 Demo failed. Check the errors above.")
    
    elif choice == "2":
        run_interactive_orgo_session()
    
    elif choice == "3":
        print("👋 Goodbye!")
    
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()