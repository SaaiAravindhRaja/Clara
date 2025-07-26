#!/usr/bin/env python3
"""
Simple test script for the AI Calendar Agent
"""

from dotenv import load_dotenv
import os

def main():
    print("🚀 Testing AI Calendar Agent...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API keys are set
    orgo_key = os.getenv('ORGO_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    
    print(f"✅ Orgo API Key: {'Set' if orgo_key else '❌ Missing'}")
    print(f"✅ OpenAI API Key: {'Set' if openai_key else '❌ Missing'}")
    print(f"✅ Anthropic API Key: {'Set' if anthropic_key else '❌ Missing'}")
    
    if not orgo_key:
        print("\n❌ ORGO_API_KEY is missing from .env file!")
        print("Please add your Orgo API key to the .env file")
        return
    
    try:
        from orgo import Computer
        
        print("\n🔧 Initializing Orgo computer...")
        computer = Computer(project_id="computer-peo2pebu")
        print("✅ Orgo computer initialized successfully!")
        
        print("\n🧪 Testing connection...")
        result = computer.prompt("Open Google Calendar")
        print(f"✅ Test successful! Result: {result}")
        
        print("\n🎉 Everything is working! You can now use the agent.")
        print("\nExample commands:")
        print("- computer.prompt('Create a meeting tomorrow at 3pm')")
        print("- computer.prompt('Find my next event')")
        print("- computer.prompt('Schedule lunch with John on Friday')")
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("Make sure you've activated the conda environment:")
        print("conda activate orgo-env")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check that your Orgo project is active")
        print("2. Verify your API keys are correct")
        print("3. Make sure you're in the orgo-env conda environment")

if __name__ == "__main__":
    main() 