#!/usr/bin/env python3
"""
🎯 Complete Setup and Run Script for Orgo AI Calendar System
This script does EVERYTHING for you - setup, install, and run
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    dependencies = [
        "python-dotenv",
        "openai",
        "orgo",
        "pillow",
        "mss"
    ]
    
    for dep in dependencies:
        try:
            print(f"   Installing {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
            print(f"   ✅ {dep} installed")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {dep} installation failed (might already be installed)")
    
    print("✅ Dependencies installation complete!")

def check_env_file():
    """Check if .env file exists and has required keys"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        return False
    
    load_dotenv()
    
    openai_key = os.getenv("OPENAI_API_KEY")
    orgo_key = os.getenv("ORGO_API_KEY")
    
    if not openai_key:
        print("❌ OPENAI_API_KEY not found in .env")
        return False
    
    if not orgo_key:
        print("❌ ORGO_API_KEY not found in .env")
        return False
    
    print("✅ API keys found in .env file")
    return True

def run_system_demo():
    """Run the complete system demo"""
    print("\n🎯 Running AI Calendar System Demo")
    print("=" * 50)
    
    # Load environment
    load_dotenv()
    
    try:
        # Import and run
        from multi_layer_prompt_system import MultiLayerCalendarSystem
        from orgo import Computer
        
        # Setup
        openai_key = os.getenv("OPENAI_API_KEY")
        orgo_key = os.getenv("ORGO_API_KEY")
        
        print("🌐 Connecting to Orgo...")
        computer = Computer(project_id="computer-ppgg5d6j")
        print("✅ Connected to Orgo successfully!")
        
        print("🧠 Initializing AI system...")
        calendar_system = MultiLayerCalendarSystem(openai_key)
        print("✅ AI system ready!")
        
        # Demo
        demo_input = "Create a diving event on August 22nd at 8am for 2 hours"
        print(f"\n📅 DEMO: {demo_input}")
        print("-" * 30)
        
        # Layer 1: Analysis
        print("🧠 Layer 1: AI analyzing your request...")
        analysis = calendar_system.prompt_engineer.analyze_user_input(demo_input)
        
        print(f"📊 Analysis Complete!")
        print(f"   Confidence: {analysis.get('confidence', 0):.1%}")
        print(f"   Extracted: {analysis.get('extracted_details', {})}")
        
        # Layer 2: Generate instruction
        print("\n🎨 Generating instruction for Orgo...")
        event_details = analysis.get('extracted_details', {})
        
        orgo_instruction = f"""
        I need you to create a calendar event in Google Calendar. Here's what to do:
        
        1. Open Firefox browser
        2. Navigate to https://calendar.google.com
        3. Click the "Create" or "+" button to create a new event
        4. Fill in these details:
           - Title: {event_details.get('title', 'Diving Event')}
           - Date: August 22nd, 2025
           - Time: 8:00 AM
           - Duration: 2 hours
        5. Save the event
        6. Confirm it appears on the calendar
        
        Please complete this task step by step.
        """
        
        print("🤖 Instruction generated!")
        print(f"📝 Instruction preview: {orgo_instruction[:100]}...")
        
        # Layer 2: Execute on Orgo
        print(f"\n🚀 Layer 2: Executing on Orgo cloud...")
        print(f"🌐 Watch the automation at: https://www.orgo.ai/projects/computer-ppgg5d6j")
        print("⏳ This may take a few moments...")
        
        result = computer.prompt(orgo_instruction)
        
        print(f"\n✅ Orgo Execution Complete!")
        print(f"📋 Result: {result}")
        
        print(f"\n🎊 SUCCESS! Your calendar event should now be created!")
        print(f"🔍 Check your Google Calendar to see the 'Diving Event' on August 22nd at 8am")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print(f"💡 Make sure your Orgo project is running and accessible")
        return False

def main():
    """Main setup and run function"""
    print("🎯 AI Calendar System - Complete Setup & Demo")
    print("=" * 50)
    
    print("🔧 Step 1: Installing dependencies...")
    install_dependencies()
    
    print("\n🔑 Step 2: Checking API keys...")
    if not check_env_file():
        print("❌ Setup failed. Please check your .env file.")
        return
    
    print("\n🚀 Step 3: Running complete demo...")
    success = run_system_demo()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 DEMO COMPLETE!")
        print("\n📋 What just happened:")
        print("1. ✅ Layer 1 (AI) analyzed your calendar request")
        print("2. ✅ Layer 2 (Orgo) executed the calendar creation")
        print("3. ✅ Your diving event should now be in Google Calendar")
        print("\n🌐 You can see the automation at:")
        print("   https://www.orgo.ai/projects/computer-ppgg5d6j")
        print("\n💡 To run again: python setup_and_run_orgo.py")
    else:
        print("\n😞 Demo failed. Please check the error messages above.")

if __name__ == "__main__":
    main()