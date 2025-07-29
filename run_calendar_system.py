#!/usr/bin/env python3
"""
🎯 AI Calendar System Launcher
This script makes it easy to run your multi-layer calendar system
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_setup():
    """Check if everything is set up correctly"""
    print("🔍 Checking system setup...")
    
    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    else:
        print("✅ OpenAI API key found")
    
    # Check imports
    try:
        from multi_layer_prompt_system import MultiLayerCalendarSystem
        print("✅ Multi-layer system ready")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    try:
        from agent_s_interface import create_calendar_event_with_agent_s
        print("✅ Agent-S interface ready")
    except ImportError as e:
        print(f"❌ Agent-S interface error: {e}")
        return False
    
    return True

def run_terminal_version():
    """Run the terminal version"""
    print("\n🚀 Starting Terminal Version...")
    print("=" * 50)
    
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    
    api_key = os.getenv("OPENAI_API_KEY")
    calendar_system = MultiLayerCalendarSystem(api_key)
    
    print("🎉 Multi-Layer Calendar System Ready!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("📅 What calendar event would you like to create? ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if user_input.strip():
            try:
                success = calendar_system.create_calendar_event(user_input)
                if success:
                    print("🎊 Event creation process completed!\n")
                else:
                    print("😞 Event creation failed. Please try again.\n")
            except Exception as e:
                print(f"❌ Error: {e}\n")
        else:
            print("Please enter a valid request.\n")

def run_gui_version():
    """Run the GUI version"""
    print("\n🚀 Starting GUI Version...")
    
    try:
        import tkinter as tk
        from gui_calendar_system import CalendarGUI
        
        root = tk.Tk()
        app = CalendarGUI(root)
        print("✅ GUI launched successfully!")
        print("💡 Look for the GUI window on your screen")
        root.mainloop()
        
    except ImportError:
        print("❌ Tkinter not available. GUI version cannot run.")
        print("💡 Try the terminal version instead.")
    except Exception as e:
        print(f"❌ GUI error: {e}")

def show_menu():
    """Show the main menu"""
    print("\n🎯 AI Calendar System")
    print("=" * 30)
    print("Choose how you want to run:")
    print("1. 🖥️  Terminal Interface (text-based)")
    print("2. 🖼️  GUI Interface (graphical)")
    print("3. 🧪 Test System")
    print("4. ❌ Exit")
    print()

def test_system():
    """Test the system"""
    print("\n🧪 Testing System...")
    
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    
    api_key = os.getenv("OPENAI_API_KEY")
    calendar_system = MultiLayerCalendarSystem(api_key)
    
    test_input = "Create a diving event on August 22nd at 8am"
    print(f"🎯 Testing with: {test_input}")
    
    try:
        analysis = calendar_system.prompt_engineer.analyze_user_input(test_input)
        print(f"\n📊 Analysis Results:")
        print(f"   Confidence: {analysis.get('confidence', 0):.1%}")
        print(f"   Extracted: {analysis.get('extracted_details', {})}")
        print(f"   Missing: {analysis.get('missing_details', [])}")
        
        if analysis.get('confidence', 0) >= 0.5:
            instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(
                analysis.get('extracted_details', {})
            )
            print(f"\n🤖 Generated Agent-S Instruction (first 200 chars):")
            print(f"   {instruction[:200]}...")
        
        print("\n✅ Test completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")

def main():
    """Main function"""
    print("🎯 AI Calendar System Launcher")
    print("=" * 40)
    
    # Check setup
    if not check_setup():
        print("\n❌ Setup check failed. Please fix the issues above.")
        return
    
    print("\n✅ All checks passed!")
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            run_terminal_version()
        elif choice == "2":
            run_gui_version()
        elif choice == "3":
            test_system()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()