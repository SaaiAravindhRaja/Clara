# AI Calendar Agent - Working Version
# Run this script to test and use the agent

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("🚀 AI Calendar Agent - Working Version")
print("=" * 50)

# Check API keys
orgo_key = os.getenv('ORGO_API_KEY')
openai_key = os.getenv('OPENAI_API_KEY')
anthropic_key = os.getenv('ANTHROPIC_API_KEY')

print(f"✅ Orgo API Key: {'Set' if orgo_key else '❌ Missing'}")
print(f"✅ OpenAI API Key: {'Set' if openai_key else '❌ Missing'}")
print(f"✅ Anthropic API Key: {'Set' if anthropic_key else '❌ Missing'}")

if not orgo_key:
    print("\n❌ ORGO_API_KEY is missing!")
    print("Please add your Orgo API key to the .env file")
    exit(1)

try:
    from orgo import Computer
    
    print("\n🔧 Initializing Orgo computer...")
    computer = Computer(project_id="computer-peo2pebu")
    print("✅ Orgo computer initialized!")
    
    print("\n🧪 Testing connection...")
    result = computer.prompt("Open Google Calendar")
    print(f"✅ Test successful!")
    
    print("\n🎉 Ready to use! Here are some example commands:")
    print("\n# Create an event:")
    print("computer.prompt('Create an event for my google calendar for diving on august 22nd 8am')")
    
    print("\n# Find events:")
    print("computer.prompt('Find my next meeting')")
    
    print("\n# Reschedule:")
    print("computer.prompt('Reschedule my 10am meeting to 2pm')")
    
    print("\n# Cancel:")
    print("computer.prompt('Cancel the yoga class on Saturday')")
    
    # Interactive mode
    print("\n" + "=" * 50)
    print("🎯 INTERACTIVE MODE")
    print("Type 'quit' to exit")
    print("=" * 50)
    
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
    print("4. Run: python test_agent.py to test the setup") 