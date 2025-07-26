#!/usr/bin/env python3
"""
Script to discover Orgo projects and help set up the correct project ID
"""

import os
import requests
from dotenv import load_dotenv

def main():
    print("🔍 Discovering your Orgo projects...")
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    orgo_api_key = os.getenv('ORGO_API_KEY')
    if not orgo_api_key:
        print("❌ ORGO_API_KEY not found in .env file")
        return
    
    print(f"✅ Using Orgo API key: {orgo_api_key[:20]}...")
    
    # Try to get projects from Orgo API
    try:
        headers = {
            'Authorization': f'Bearer {orgo_api_key}',
            'Content-Type': 'application/json'
        }
        
        # Try different endpoints to find projects
        endpoints = [
            'https://api.orgo.ai/v1/projects',
            'https://api.orgo.ai/projects',
            'https://app.orgo.ai/api/projects'
        ]
        
        for endpoint in endpoints:
            try:
                print(f"🔍 Trying endpoint: {endpoint}")
                response = requests.get(endpoint, headers=headers, timeout=10)
                print(f"Response status: {response.status_code}")
                
                if response.status_code == 200:
                    projects = response.json()
                    print("✅ Found projects!")
                    print("\n📋 Your Orgo Projects:")
                    for i, project in enumerate(projects.get('data', projects), 1):
                        project_id = project.get('id', project.get('project_id', 'Unknown'))
                        name = project.get('name', project.get('title', 'Unnamed'))
                        print(f"  {i}. {name} (ID: {project_id})")
                    
                    print(f"\n💡 Update your .orgo/project.json with one of these project IDs")
                    return
                    
            except Exception as e:
                print(f"❌ Failed with endpoint {endpoint}: {e}")
                continue
        
        print("\n❌ Could not find projects with any endpoint")
        print("\n🔧 Manual Setup Instructions:")
        print("1. Go to https://app.orgo.ai/")
        print("2. Sign in with your account")
        print("3. Look for your project ID in the URL or dashboard")
        print("4. Update .orgo/project.json with the correct project ID")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔧 Manual Setup Instructions:")
        print("1. Go to https://app.orgo.ai/")
        print("2. Sign in with your account")
        print("3. Create a new project or find existing one")
        print("4. Get the project ID and update .orgo/project.json")

if __name__ == "__main__":
    main() 