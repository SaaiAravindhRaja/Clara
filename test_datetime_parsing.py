#!/usr/bin/env python3
"""
Test the improved date/time parsing
"""

import os
from multi_layer_prompt_system import MultiLayerCalendarSystem

# Load API key from environment variables
# Make sure to set OPENAI_API_KEY in your .env file or environment
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")

def test_datetime_parsing():
    """Test various date/time inputs"""
    calendar_system = MultiLayerCalendarSystem(os.environ["OPENAI_API_KEY"])
    
    test_cases = [
        "SMU GYM on August 22nd at 8am for 2 hours",
        "diving event August 22nd 8am",
        "meeting tomorrow at 2pm",
        "gym session next Friday at 8:30am"
    ]
    
    print("🧪 Testing Date/Time Parsing")
    print("=" * 50)
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"\n🔍 Test {i}: {test_input}")
        print("-" * 30)
        
        try:
            analysis = calendar_system.prompt_engineer.analyze_user_input(test_input)
            
            print(f"📊 Confidence: {analysis.get('confidence', 0):.1%}")
            print(f"📅 Extracted Details:")
            for key, value in analysis.get('extracted_details', {}).items():
                print(f"   {key}: {value}")
            
            if analysis.get('missing_details'):
                print(f"❓ Missing: {analysis.get('missing_details')}")
            
            # Generate instruction to see how it formats
            if analysis.get('confidence', 0) >= 0.5:
                instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(
                    analysis.get('extracted_details', {})
                )
                print(f"🤖 Instruction preview: {instruction[:150]}...")
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_datetime_parsing()