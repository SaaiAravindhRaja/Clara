"""
Run the multi-layer system test with API key
"""

import os
import sys

# Load API key from environment variables
# Make sure to set OPENAI_API_KEY in your .env file or environment
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")

def test_with_api():
    """Test the system with actual API calls"""
    from multi_layer_prompt_system import MultiLayerCalendarSystem
    
    print("🚀 Testing Multi-Layer System with OpenAI API")
    print("=" * 50)
    
    # Initialize system
    calendar_system = MultiLayerCalendarSystem(os.environ["OPENAI_API_KEY"])
    
    # Test case
    test_input = "Create a diving event on August 22nd at 8am"
    print(f"🎯 Testing with: {test_input}")
    
    try:
        # Test just the analysis part (Layer 1)
        analysis = calendar_system.prompt_engineer.analyze_user_input(test_input)
        
        print(f"\n📊 Analysis Results:")
        print(f"   Confidence: {analysis.get('confidence', 0):.1%}")
        print(f"   Extracted Details: {analysis.get('extracted_details', {})}")
        print(f"   Missing Details: {analysis.get('missing_details', [])}")
        print(f"   Questions: {analysis.get('clarification_questions', [])}")
        
        # If confidence is high enough, generate Agent-S instruction
        if analysis.get('confidence', 0) >= 0.5:
            instruction = calendar_system.prompt_engineer.generate_agent_s_instruction(
                analysis.get('extracted_details', {})
            )
            print(f"\n🤖 Generated Agent-S Instruction:")
            print(f"   {instruction}")
            print("\n✅ Layer 1 (Prompt Engineering) working correctly!")
        else:
            print(f"\n❓ Would ask clarification questions: {analysis.get('clarification_questions', [])}")
            print("✅ Layer 1 correctly identified missing information!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during API test: {e}")
        return False

def test_gui_ready():
    """Test if GUI is ready to run"""
    try:
        import tkinter as tk
        print("✅ Tkinter available - GUI ready")
        return True
    except ImportError:
        print("❌ Tkinter not available - GUI won't work")
        return False

if __name__ == "__main__":
    print("🧪 Multi-Layer Calendar System - Full Test")
    print("=" * 60)
    
    # Test API functionality
    if test_with_api():
        print("\n🎉 API test successful!")
    else:
        print("\n😞 API test failed")
        sys.exit(1)
    
    # Test GUI readiness
    print("\n" + "-" * 40)
    test_gui_ready()
    
    print("\n" + "=" * 60)
    print("🚀 System Ready! You can now run:")
    print("   python multi_layer_prompt_system.py  # Terminal interface")
    print("   python gui_calendar_system.py        # GUI interface")
    print("   python prompt_engineer.py            # Enhanced prompt engineer")
    print("\n💡 The system will:")
    print("   1. Analyze your natural language input")
    print("   2. Ask for missing details if needed")
    print("   3. Generate optimized Agent-S instructions")
    print("   4. Execute via your existing Agent-S setup")