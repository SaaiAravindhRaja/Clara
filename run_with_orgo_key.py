#!/usr/bin/env python3
"""
🎯 Run AI Calendar System with Orgo API Key
Direct execution on https://www.orgo.ai/projects/computer-ppgg5d6j
"""

import os
import sys

# Load API keys from environment variables
# Make sure to set these in your .env file or environment
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")
if not os.environ.get("ORGO_API_KEY"):
    raise ValueError("ORGO_API_KEY environment variable is required")

def test_orgo_connection():
    """Test Orgo connection with API key"""
    print("🧪 Testing Orgo connection...")
    
    try:
        from orgo import Computer
        
        # Initialize with project ID and API key
        computer = Computer(
            project_id="computer-ppgg5d6j",
            api_key="sk_live_b76d3db0cd60ca4fd3eb199b59ca3d1ff4526ea309dc4732"
        )
        
        # Test with simple prompt
        result = computer.prompt("Take a screenshot and describe what you see on the screen in one sentence.")
        
        print("✅ Orgo connection successful!")
        print(f"📊 Test result: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Orgo connection failed: {e}")
        return False

def run_calendar_demo():
    """Run calendar creation demo on Orgo"""
    print("🎯 Running Calendar Demo on Orgo Cloud")
    print("🌐 Watch at: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 60)
    
    try:
        from orgo import Computer
        
        # Initialize Orgo with API key
        computer = Computer(
            project_id="computer-ppgg5d6j",
            api_key="sk_live_b76d3db0cd60ca4fd3eb199b59ca3d1ff4526ea309dc4732"
        )
        
        # Calendar creation instruction
        instruction = """
Please help me create a calendar event. Follow these steps:

1. Open Firefox browser (if not already open)
2. Navigate to https://calendar.google.com
3. Wait for Google Calendar to load completely
4. Look for and click the "Create" button or "+" button to create a new event
5. Fill in the event details:
   - Title: "Diving Event"
   - Date: August 22nd, 2025
   - Time: 8:00 AM
   - Duration: 2 hours (so end time should be 10:00 AM)
6. Save the event by clicking the "Save" button
7. Confirm the event appears in the calendar

Please execute these steps carefully and let me know if you encounter any issues or need clarification.
"""
        
        print("🚀 Sending calendar creation instruction to Orgo...")
        print("⏳ This may take a few moments...")
        
        result = computer.prompt(instruction)
        
        print("✅ Orgo execution completed!")
        print(f"📊 Result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during Orgo execution: {e}")
        return False

def run_multi_layer_system():
    """Run the full multi-layer system with Orgo"""
    print("🎯 Multi-Layer AI Calendar System")
    print("🌐 Executing on: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 60)
    
    # Get user input
    user_input = input("📅 What calendar event would you like to create? ")
    
    if not user_input.strip():
        user_input = "Create a diving event on August 22nd at 8am for 2 hours"
        print(f"🎯 Using demo input: {user_input}")
    
    try:
        # Layer 1: Prompt Engineering
        print("\n🧠 Layer 1: Analyzing with Prompt Engineering LLM...")
        
        from multi_layer_prompt_system import MultiLayerCalendarSystem
        calendar_system = MultiLayerCalendarSystem(os.environ["OPENAI_API_KEY"])
        
        # Analyze user input
        analysis = calendar_system.prompt_engineer.analyze_user_input(user_input)
        
        print(f"📊 Analysis Results:")
        print(f"   Confidence: {analysis.get('confidence', 0):.1%}")
        print(f"   Extracted: {analysis.get('extracted_details', {})}")
        print(f"   Missing: {analysis.get('missing_details', [])}")
        
        # Handle missing information
        if analysis.get('confidence', 0) < 0.8 and analysis.get('clarification_questions'):
            print(f"❓ Questions: {analysis.get('clarification_questions', [])}")
            
            # For demo, provide default answers
            user_answers = {}
            for question in analysis.get('clarification_questions', []):
                if "duration" in question.lower() or "long" in question.lower():
                    user_answers[question] = "2 hours"
                elif "location" in question.lower() or "where" in question.lower():
                    user_answers[question] = "Local diving center"
            
            if user_answers:
                print(f"🤖 Auto-answering: {user_answers}")
                event_details = calendar_system.prompt_engineer.refine_event_details(
                    analysis.get('extracted_details', {}), 
                    user_answers
                )
            else:
                event_details = analysis.get('extracted_details', {})
        else:
            event_details = analysis.get('extracted_details', {})
        
        # Generate optimized instruction
        agent_instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(event_details)
        
        print(f"\n🤖 Generated optimized instruction for Orgo")
        print(f"📝 Instruction length: {len(agent_instruction)} characters")
        
        # Layer 2: Execute on Orgo
        print(f"\n🌐 Layer 2: Executing on Orgo Cloud...")
        print(f"🎯 Watch the automation at: https://www.orgo.ai/projects/computer-ppgg5d6j")
        print("⏳ This may take a few moments...")
        
        from orgo import Computer
        computer = Computer(
            project_id="computer-ppgg5d6j",
            api_key="sk_live_b76d3db0cd60ca4fd3eb199b59ca3d1ff4526ea309dc4732"
        )
        
        result = computer.prompt(agent_instruction)
        
        print(f"\n✅ Multi-layer system execution completed!")
        print(f"📊 Final result: {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during multi-layer execution: {e}")
        return False

def main():
    """Main function"""
    print("🎯 AI Calendar System - Orgo Edition")
    print("🔑 Using your Orgo API key")
    print("🌐 Target: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 60)
    
    # Test connection first
    if not test_orgo_connection():
        print("\n❌ Orgo connection test failed!")
        print("Please check:")
        print("1. Your Orgo project is running")
        print("2. Your API key is correct")
        print("3. Your internet connection")
        return
    
    print("\n🎉 Orgo connection successful!")
    print("\nChoose your option:")
    print("1. 🎬 Quick Demo (simple calendar event)")
    print("2. 🎯 Full Multi-Layer System (AI-powered)")
    print("3. ❌ Exit")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n🎬 Running Quick Demo...")
        success = run_calendar_demo()
        if success:
            print("\n🎉 Demo completed! Check your Orgo desktop.")
        else:
            print("\n😞 Demo failed.")
    
    elif choice == "2":
        print("\n🎯 Running Full Multi-Layer System...")
        success = run_multi_layer_system()
        if success:
            print("\n🎉 Multi-layer system completed!")
        else:
            print("\n😞 Multi-layer system failed.")
    
    elif choice == "3":
        print("👋 Goodbye!")
    
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()