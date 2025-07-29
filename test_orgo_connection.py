#!/usr/bin/env python3
"""
Test Orgo connection and understand the requirements
"""

import os

# Load API keys from environment variables
# Make sure to set these in your .env file or environment
if not os.environ.get("ORGO_API_KEY"):
    raise ValueError("ORGO_API_KEY environment variable is required")
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is required")

def test_orgo_import():
    """Test if we can import Orgo"""
    try:
        from orgo import Computer
        print("✅ Orgo library imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import Orgo: {e}")
        return False

def test_orgo_initialization():
    """Test different ways to initialize Orgo"""
    from orgo import Computer
    
    print("🧪 Testing Orgo initialization methods...")
    
    # Method 1: With project_id only
    try:
        computer = Computer(project_id="computer-ppgg5d6j")
        print("✅ Method 1: Initialized with project_id only")
        return computer
    except Exception as e:
        print(f"❌ Method 1 failed: {e}")
    
    # Method 2: With project_id and api_key
    try:
        computer = Computer(
            project_id="computer-ppgg5d6j",
            api_key="sk_live_b76d3db0cd60ca4fd3eb199b59ca3d1ff4526ea309dc4732"
        )
        print("✅ Method 2: Initialized with project_id and api_key")
        return computer
    except Exception as e:
        print(f"❌ Method 2 failed: {e}")
    
    # Method 3: Check what parameters Computer accepts
    try:
        import inspect
        sig = inspect.signature(Computer.__init__)
        print(f"🔍 Computer.__init__ parameters: {list(sig.parameters.keys())}")
    except Exception as e:
        print(f"❌ Could not inspect Computer parameters: {e}")
    
    return None

def test_simple_prompt(computer):
    """Test a simple prompt"""
    try:
        print("🧪 Testing simple prompt...")
        result = computer.prompt("What can you see on the screen right now?")
        print(f"✅ Prompt successful!")
        print(f"📊 Result: {result[:200]}...")
        return True
    except Exception as e:
        print(f"❌ Prompt failed: {e}")
        return False

def main():
    print("🧪 Orgo Connection Test")
    print("🌐 Target: https://www.orgo.ai/projects/computer-ppgg5d6j")
    print("🔑 API Key: sk_live_b76d3db0cd60ca4fd3eb199b59ca3d1ff4526ea309dc4732")
    print("=" * 60)
    
    # Test import
    if not test_orgo_import():
        return
    
    # Test initialization
    computer = test_orgo_initialization()
    if not computer:
        print("❌ Could not initialize Orgo Computer")
        return
    
    # Test simple prompt
    if test_simple_prompt(computer):
        print("\n🎉 Orgo connection fully working!")
        print("🚀 Ready to run calendar system!")
    else:
        print("\n😞 Orgo connection partially working but prompts fail")

if __name__ == "__main__":
    main()