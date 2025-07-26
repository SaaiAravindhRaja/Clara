#!/usr/bin/env python3
"""
Script to help set up Orgo project
"""

import os
import json
from dotenv import load_dotenv

def main():
    print("🚀 Setting up Orgo Project for AI Calendar Agent")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    print("\n📋 Current Setup:")
    print(f"✅ Orgo API Key: {os.getenv('ORGO_API_KEY', 'Not set')[:20]}...")
    print(f"✅ OpenAI API Key: {os.getenv('OPENAI_API_KEY', 'Not set')[:20]}...")
    print(f"✅ Anthropic API Key: {os.getenv('ANTHROPIC_API_KEY', 'Not set')[:20]}...")
    
    # Check current project ID
    try:
        with open('.orgo/project.json', 'r') as f:
            current_config = json.load(f)
            current_project_id = current_config.get('project_id', 'None')
            print(f"📁 Current Project ID: {current_project_id}")
    except FileNotFoundError:
        print("📁 No .orgo/project.json found")
        current_project_id = None
    
    print("\n🔧 Next Steps:")
    print("1. Go to https://app.orgo.ai/")
    print("2. Sign in with your account")
    print("3. Create a new project or find an existing one")
    print("4. Get the project ID from the URL or dashboard")
    
    # Ask user for project ID
    print("\n" + "=" * 50)
    new_project_id = input("🤖 Enter your Orgo Project ID: ").strip()
    
    if not new_project_id:
        print("❌ No project ID provided")
        return
    
    # Update project.json
    try:
        os.makedirs('.orgo', exist_ok=True)
        with open('.orgo/project.json', 'w') as f:
            json.dump({'project_id': new_project_id}, f, indent=2)
        
        print(f"✅ Updated .orgo/project.json with project ID: {new_project_id}")
        
        # Test the connection
        print("\n🧪 Testing connection...")
        test_connection(new_project_id)
        
    except Exception as e:
        print(f"❌ Error updating project.json: {e}")

def test_connection(project_id):
    """Test the connection with the new project ID"""
    try:
        from orgo import Computer
        
        print(f"🔧 Initializing Orgo computer with project ID: {project_id}")
        computer = Computer(project_id=project_id)
        print("✅ Orgo computer initialized successfully!")
        
        print("\n🧪 Testing with a simple prompt...")
        result = computer.prompt("Open Google Calendar")
        print(f"✅ Test successful! Result: {result}")
        
        print("\n🎉 Everything is working! You can now use the AI Calendar Agent.")
        print("\n💡 Try these commands:")
        print("- computer.prompt('Create a meeting tomorrow at 3pm')")
        print("- computer.prompt('Find my next event')")
        print("- computer.prompt('Schedule lunch with John on Friday')")
        
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure the project ID is correct")
        print("2. Check that your Orgo project is active")
        print("3. Verify your API key has access to this project")

if __name__ == "__main__":
    main() 