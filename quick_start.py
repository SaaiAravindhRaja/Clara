#!/usr/bin/env python3
"""
Quick Start Script for AI Calendar Agent
This will help you get everything working step by step
"""

import os
import json
from dotenv import load_dotenv

def main():
    print("🚀 AI Calendar Agent - Quick Start")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Check API keys
    orgo_key = os.getenv('ORGO_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    print("\n📋 API Keys Status:")
    print(f"✅ Orgo: {'Set' if orgo_key else '❌ Missing'}")
    print(f"✅ OpenAI: {'Set' if openai_key else '❌ Missing'}")
    print(f"✅ Anthropic: {'Set' if anthropic_key else '❌ Missing'}")
    
    if not all([orgo_key, openai_key, anthropic_key]):
        print("\n❌ Missing API keys. Please check your .env file")
        return
    
    # Check project ID
    try:
        with open('.orgo/project.json', 'r') as f:
            config = json.load(f)
            project_id = config.get('project_id')
            print(f"\n📁 Project ID: {project_id}")
    except FileNotFoundError:
        print("\n❌ No .orgo/project.json found")
        print("Please run: python setup_orgo_project.py")
        return
    
    if not project_id:
        print("\n❌ No project ID found")
        print("Please run: python setup_orgo_project.py")
        return
    
    # Test connection
    print(f"\n🧪 Testing connection with project ID: {project_id}")
    test_connection(project_id)

def test_connection(project_id):
    """Test the Orgo connection"""
    try:
        from orgo import Computer
        
        print("🔧 Initializing Orgo computer...")
        computer = Computer(project_id=project_id)
        print("✅ Orgo computer initialized!")
        
        print("\n🧪 Testing with Google Calendar...")
        result = computer.prompt("Open Google Calendar")
        print(f"✅ Success! Result: {result}")
        
        print("\n🎉 CONGRATULATIONS! Everything is working!")
        print("\n" + "=" * 50)
        print("🎯 You can now use the AI Calendar Agent!")
        print("=" * 50)
        
        # Interactive mode
        print("\n💡 Try these example commands:")
        print("1. Create a meeting: 'Schedule a meeting with John tomorrow at 3pm'")
        print("2. Find events: 'What's my next meeting?'")
        print("3. Reschedule: 'Move my 2pm meeting to Friday'")
        print("4. Cancel: 'Cancel the yoga class on Saturday'")
        
        print("\n🤖 Interactive Mode (type 'quit' to exit):")
        print("-" * 30)
        
        while True:
            try:
                user_input = input("\n🤖 Enter your calendar command: ")
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                print(f"🔄 Processing: {user_input}")
                result = computer.prompt(user_input)
                print(f"✅ Result: {result}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Try again or type 'quit' to exit")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure your Orgo project is active")
        print("2. Check that your API keys are correct")
        print("3. Verify the project ID is valid")
        print("4. Try running: python setup_orgo_project.py")

if __name__ == "__main__":
    main() 