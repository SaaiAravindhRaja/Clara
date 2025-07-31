"""
Test script for the Multi-Layer Calendar System
"""

import os
from multi_layer_prompt_system import MultiLayerCalendarSystem

def test_system():
    """Test the multi-layer system with sample inputs"""
    
    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your OpenAI API key in your environment variables.")
        return
    
    # Initialize system
    print("🚀 Initializing Multi-Layer Calendar System...")
    calendar_system = MultiLayerCalendarSystem(api_key)
    
    # Test cases
    test_cases = [
        "Create a diving event on August 22nd at 8am",
        "Schedule a meeting with John tomorrow at 2pm",
        "Book a dentist appointment next Friday",
        "Team standup every Monday at 9am for 30 minutes"
    ]
    
    print("🧪 Running test cases...\n")
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"🔍 Test Case {i}: {test_input}")
        print("-" * 60)
        
        try:
            # Just test the prompt engineering layer (without Agent-S execution)
            analysis = calendar_system.prompt_engineer.analyze_user_input(test_input)
            print(f"📊 Analysis Results:")
            print(f"   Confidence: {analysis['confidence']:.1%}")
            print(f"   Extracted: {analysis['extracted_details']}")
            print(f"   Missing: {analysis['missing_details']}")
            
            if analysis['confidence'] >= 0.8:
                # Generate Agent-S instruction
                instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(
                    analysis['extracted_details']
                )
                print(f"🤖 Generated Agent-S Instruction:")
                print(f"   {instruction[:100]}...")
                print("✅ Test passed!")
            else:
                print("❓ Would require user clarification")
                print(f"   Questions: {analysis['clarification_questions']}")
                
        except Exception as e:
            print(f"❌ Test failed: {e}")
        
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    test_system()