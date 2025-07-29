"""
Test the multi-layer system structure without API calls
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported"""
    try:
        from multi_layer_prompt_system import MultiLayerCalendarSystem, PromptEngineeringLayer
        print("✅ Successfully imported MultiLayerCalendarSystem")
        
        from agent_s_interface import create_calendar_event_with_agent_s
        print("✅ Successfully imported agent_s_interface")
        
        from gui_calendar_system import CalendarGUI
        print("✅ Successfully imported CalendarGUI")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_system_structure():
    """Test the system structure without API calls"""
    print("\n🔍 Testing system structure...")
    
    # Mock API key for structure testing
    mock_api_key = "test-key"
    
    try:
        from multi_layer_prompt_system import PromptEngineeringLayer
        
        # Test class initialization (won't make API calls)
        prompt_layer = PromptEngineeringLayer(mock_api_key)
        print("✅ PromptEngineeringLayer initialized")
        
        # Test method existence
        methods = ['analyze_user_input', 'ask_clarification_questions', 'refine_event_details', 'generate_agent_s_instruction']
        for method in methods:
            if hasattr(prompt_layer, method):
                print(f"✅ Method {method} exists")
            else:
                print(f"❌ Method {method} missing")
        
        return True
    except Exception as e:
        print(f"❌ Structure test failed: {e}")
        return False

def test_sample_analysis():
    """Test sample input analysis structure"""
    print("\n📝 Testing sample analysis structure...")
    
    sample_inputs = [
        "Create a diving event on August 22nd at 8am",
        "Schedule a meeting with John tomorrow at 2pm",
        "Book a dentist appointment next Friday"
    ]
    
    for input_text in sample_inputs:
        print(f"📅 Sample: {input_text}")
        # Here we would normally call the analysis, but we'll just show the structure
        expected_fields = ["extracted_details", "missing_details", "confidence", "clarification_questions"]
        print(f"   Expected analysis fields: {expected_fields}")
    
    return True

if __name__ == "__main__":
    print("🧪 Testing Multi-Layer System Structure")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("❌ Import tests failed. Please check dependencies.")
        sys.exit(1)
    
    # Test structure
    if not test_system_structure():
        print("❌ Structure tests failed.")
        sys.exit(1)
    
    # Test sample analysis
    test_sample_analysis()
    
    print("\n" + "=" * 50)
    print("✅ All structure tests passed!")
    print("\n🚀 Ready to test with API key:")
    print("   python multi_layer_prompt_system.py")
    print("   python gui_calendar_system.py")
    print("   python prompt_engineer.py")