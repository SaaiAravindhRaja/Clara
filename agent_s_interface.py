import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import Orgo first, then fall back to Agent-S
try:
    from orgo import Computer
    ORGO_AVAILABLE = True
except ImportError:
    ORGO_AVAILABLE = False

# Try Agent-S imports
try:
    from gui_agents.core.AgentS import UIAgent
    from PIL import Image
    from mss import mss
    AGENT_S_AVAILABLE = True
except ImportError:
    AGENT_S_AVAILABLE = False

def get_screenshot():
    """
    Captures a screenshot of the primary monitor.
    """
    with mss() as sct:
        # Get information of monitor 1
        monitor = sct.monitors[1]
        # Grab the data
        sct_img = sct.grab(monitor)
        # Convert to PIL Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        return img

def create_calendar_event_with_orgo(instruction: str):
    """
    Sends an instruction to Orgo to create a calendar event.
    This runs on the Orgo cloud desktop.
    """
    print(f"🌐 Using Orgo for calendar event creation:")
    print(f"🎯 Instruction: {instruction}")
    print(f"🌐 Watch at: https://www.orgo.ai/projects/computer-ppgg5d6j")

    try:
        # Initialize Orgo Computer
        project_id = "computer-ppgg5d6j"
        computer = Computer(project_id=project_id)
        
        print("🚀 Sending instruction to Orgo cloud desktop...")
        result = computer.prompt(instruction)
        
        print(f"✅ Orgo Result: {result}")
        return result

    except Exception as e:
        print(f"❌ Error during Orgo interaction: {e}")
        print("Please ensure Orgo is properly configured and your project is running.")
        return None

def create_calendar_event_with_agent_s(instruction: str):
    """
    Sends an instruction to create a calendar event.
    Tries Orgo first, then falls back to Agent-S.
    """
    print(f"🎯 Creating calendar event with instruction:")
    print(f"   {instruction[:100]}...")
    
    # Try Orgo first (preferred for cloud execution)
    if ORGO_AVAILABLE:
        print("🌐 Using Orgo cloud desktop...")
        return create_calendar_event_with_orgo(instruction)
    
    # Fall back to Agent-S
    elif AGENT_S_AVAILABLE:
        print("🤖 Using Agent-S local execution...")
        return create_calendar_event_with_local_agent_s(instruction)
    
    else:
        print("❌ Neither Orgo nor Agent-S is available!")
        print("Please install one of them:")
        print("   pip install orgo")
        print("   or install Agent-S following the setup guide")
        return None

def create_calendar_event_with_local_agent_s(instruction: str):
    """
    Local Agent-S execution (fallback method)
    """
    try:
        # Initialize UIAgent with OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")
        agent = UIAgent(api_key=api_key, model="gpt-4o")

        # Capture screenshot
        screenshot = get_screenshot()

        if screenshot:
            print("Sending instruction and screenshot to Agent-S...")
            result = agent.run(screenshot=screenshot, instruction=instruction)
            print(f"Agent-S Result: {result}")
            return result
        else:
            print("Could not capture screenshot. Agent-S interaction aborted.")
            return None

    except Exception as e:
        print(f"Error during Agent-S interaction: {e}")
        print("Please ensure Agent-S is installed and configured correctly.")
        return None

if __name__ == "__main__":
    # Example usage (for testing the interface)
    test_instruction = "Open Firefox, navigate to Google Calendar, and create an event titled 'Team Meeting' on August 1st, 2025 at 10 AM for 1 hour."
    create_calendar_event_with_agent_s(test_instruction)