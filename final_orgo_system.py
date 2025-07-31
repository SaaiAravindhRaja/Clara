#!/usr/bin/env python3
"""
🎯 FINAL AI Calendar System - Complete Orgo Implementation
This script runs your multi-layer system on https://www.orgo.ai/projects/computer-ppgg5d6j
"""

import os

# Load API keys from environment variables
# Make sure to set these in your .env file or environment
required_keys = ["OPENAI_API_KEY", "ORGO_API_KEY", "ANTHROPIC_API_KEY"]
for key in required_keys:
    if not os.environ.get(key):
        raise ValueError(f"{key} environment variable is required")

def test_orgo_connection():
    """Test Orgo connection with all API keys"""
    print("🧪 Testing Orgo connection with all API keys...")
    
    try:
        from orgo import Computer
        
        computer = Computer(project_id="computer-ppgg5d6j")
        
        # Test with simple prompt
        result = computer.prompt("Take a screenshot and tell me what you can see on the screen in one sentence.")
        
        print("✅ Orgo connection successful!")
        print(f"📊 Test result: {result}")
        return computer
        
    except Exception as e:
        print(f"❌ Orgo connection failed: {e}")
        return None

def run_complete_calendar_demo():
    """Run the complete multi-layer calendar system"""
    print("🎯 COMPLETE AI CALENDAR SYSTEM DEMO")
    print("🌐 Running on: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 60)
    
    # Test Orgo connection
    computer = test_orgo_connection()
    if not computer:
        print("❌ Cannot proceed without Orgo connection")
        return False
    
    # Initialize multi-layer system
    print("\n🧠 Initializing Multi-Layer AI System...")
    
    try:
        from multi_layer_prompt_system import MultiLayerCalendarSystem
        calendar_system = MultiLayerCalendarSystem(os.environ["OPENAI_API_KEY"])
        print("✅ Multi-layer system initialized!")
    except Exception as e:
        print(f"❌ Failed to initialize multi-layer system: {e}")
        return False
    
    # Demo input
    demo_input = "Create a diving event on August 22nd at 8am for 2 hours"
    print(f"\n📅 DEMO INPUT: {demo_input}")
    print("-" * 40)
    
    # LAYER 1: Prompt Engineering LLM
    print("🧠 LAYER 1: Prompt Engineering LLM Analysis...")
    
    try:
        analysis = calendar_system.prompt_engineer.analyze_user_input(demo_input)
        
        print(f"📊 Analysis Results:")
        print(f"   ✅ Confidence: {analysis.get('confidence', 0):.1%}")
        print(f"   ✅ Extracted Details: {analysis.get('extracted_details', {})}")
        print(f"   ✅ Missing Details: {analysis.get('missing_details', [])}")
        
        # Handle missing information
        event_details = analysis.get('extracted_details', {})
        if analysis.get('confidence', 0) < 0.8:
            print(f"   🤖 Auto-completing missing details...")
            # Auto-complete for demo
            if not event_details.get('duration'):
                event_details['duration'] = '2 hours'
            if not event_details.get('location'):
                event_details['location'] = 'Local diving center'
        
        print(f"   ✅ Final Event Details: {event_details}")
        
    except Exception as e:
        print(f"❌ Layer 1 failed: {e}")
        return False
    
    # Generate optimized instruction
    print(f"\n🎨 Generating optimized instruction for Orgo...")
    
    try:
        agent_instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(event_details)
        print(f"✅ Instruction generated ({len(agent_instruction)} characters)")
        print(f"📝 Preview: {agent_instruction[:150]}...")
    except Exception as e:
        print(f"❌ Instruction generation failed: {e}")
        return False
    
    # LAYER 2: Orgo Execution
    print(f"\n🌐 LAYER 2: Orgo Cloud Execution...")
    print(f"🎯 Watch the automation at: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print(f"⏳ This may take 30-60 seconds...")
    
    try:
        result = computer.prompt(agent_instruction)
        
        print(f"\n✅ ORGO EXECUTION COMPLETED!")
        print(f"📊 Result: {result}")
        
        print(f"\n🎉 SUCCESS! Your multi-layer system worked!")
        print(f"📋 What happened:")
        print(f"   1. ✅ Layer 1 (OpenAI) analyzed your request")
        print(f"   2. ✅ Layer 1 generated optimized instructions")
        print(f"   3. ✅ Layer 2 (Orgo) executed the calendar creation")
        print(f"   4. ✅ Your diving event should now be in Google Calendar!")
        
        return True
        
    except Exception as e:
        print(f"❌ Layer 2 (Orgo execution) failed: {e}")
        return False

def run_interactive_session():
    """Run interactive session"""
    print("🎯 INTERACTIVE AI CALENDAR SYSTEM")
    print("🌐 Running on: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 50)
    
    # Setup
    computer = test_orgo_connection()
    if not computer:
        return
    
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    calendar_system = MultiLayerCalendarSystem(os.environ["OPENAI_API_KEY"])
    
    print("🎉 System ready! Type 'quit' to exit")
    print()
    
    while True:
        user_input = input("📅 What calendar event would you like to create? ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if user_input.strip():
            try:
                print("🧠 Layer 1: Analyzing...")
                analysis = calendar_system.prompt_engineer.analyze_user_input(user_input)
                
                print(f"📊 Confidence: {analysis.get('confidence', 0):.1%}")
                
                # Handle missing details
                event_details = analysis.get('extracted_details', {})
                if analysis.get('confidence', 0) < 0.8 and analysis.get('clarification_questions'):
                    for question in analysis.get('clarification_questions', []):
                        answer = input(f"❓ {question} ")
                        if answer.strip():
                            if 'duration' in question.lower():
                                event_details['duration'] = answer
                            elif 'location' in question.lower():
                                event_details['location'] = answer
                
                # Generate and execute
                instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(event_details)
                
                print("🌐 Layer 2: Executing on Orgo...")
                result = computer.prompt(instruction)
                
                print(f"✅ Done! Result: {result[:100]}...")
                print()
                
            except Exception as e:
                print(f"❌ Error: {e}")
                print()

def main():
    """Main function"""
    print("🎯 AI CALENDAR SYSTEM - FINAL VERSION")
    print("🔑 All API keys configured")
    print("🌐 Target: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("=" * 60)
    
    print("Choose your option:")
    print("1. 🎬 Complete Demo (shows both layers working)")
    print("2. 💬 Interactive Session (create your own events)")
    print("3. ❌ Exit")
    print()
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        print("\n🎬 Running Complete Demo...")
        success = run_complete_calendar_demo()
        if success:
            print("\n🎊 DEMO SUCCESSFUL!")
            print("🌐 Check your Orgo desktop and Google Calendar!")
        else:
            print("\n😞 Demo failed. Check errors above.")
    
    elif choice == "2":
        print("\n💬 Starting Interactive Session...")
        run_interactive_session()
    
    elif choice == "3":
        print("👋 Goodbye!")
    
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()