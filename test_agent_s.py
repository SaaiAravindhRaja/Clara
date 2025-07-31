import os
from gui_agents.core.AgentS import UIAgent
from PIL import Image
from mss import mss

def get_screenshot():
    """
    Captures a screenshot of the primary monitor.
    """
    with mss() as sct:
        # Get information of monitor 1 (usually the primary display)
        monitor = sct.monitors[1]
        # Grab the data
        sct_img = sct.grab(monitor)
        # Convert to PIL Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        return img

if __name__ == "__main__":
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set.")

        print("Initializing UIAgent...")
        # Initialize UIAgent with OpenAI
        agent = UIAgent(api_key=api_key, model="gpt-4o")

        print("Capturing screenshot...")
        screenshot = get_screenshot()

        if screenshot:
            print("Sending a test instruction to Agent-S (gui-agents)...")
            # This instruction will attempt to open Firefox and navigate to example.com
            instruction = "Open Firefox and navigate to https://www.example.com. Then close the browser."
            result = agent.run(screenshot=screenshot, instruction=instruction)
            print(f"Agent-S Test Result: {result}")
        else:
            print("Could not capture screenshot. Ensure 'mss' is working and display is accessible.")

    except Exception as e:
        print(f"Error during Agent-S test: {e}")
        print("Please ensure Agent-S (gui-agents) is installed and configured correctly, and API keys are set.")