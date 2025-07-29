
"""
Legacy Prompt Engineer - Now integrated with Multi-Layer System
This file is kept for backward compatibility
"""

import datetime
import os
from agent_s_interface import create_calendar_event_with_agent_s
from multi_layer_prompt_system import MultiLayerCalendarSystem

def get_event_details_from_user():
    """
    LEGACY: Interactively gathers calendar event details from the user.
    Consider using MultiLayerCalendarSystem for better experience.
    """
    print("Let's create a new calendar event.")
    title = input("What is the title of the event? ")

    date_str = input("What is the date of the event? (e.g., August 22nd, 2025) ")
    # Basic date parsing, can be improved for robustness
    try:
        # Attempt to parse common date formats
        event_date = datetime.datetime.strptime(date_str, "%B %dth, %Y").date()
    except ValueError:
        try:
            event_date = datetime.datetime.strptime(date_str, "%B %d, %Y").date()
        except ValueError:
            print("Could not parse date. Please try again with a format like 'August 22nd, 2025'.")
            return None, None, None, None, None

    time_str = input("What is the start time? (e.g., 8 AM, 14:00) ")
    # Basic time parsing
    try:
        # Attempt to parse common time formats
        event_time = datetime.datetime.strptime(time_str, "%I %p").time()
    except ValueError:
        try:
            event_time = datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            print("Could not parse time. Please try again with a format like '8 AM' or '14:00'.")
            return None, None, None, None, None

    duration = input("How long will the event last? (e.g., 1 hour, 30 minutes) ")
    location = input("Where will the event take place? (optional) ")

    return title, event_date, event_time, duration, location

def generate_agent_s_instruction(title, date, time, duration, location):
    """
    LEGACY: Generates a detailed instruction for Agent-S based on gathered event details.
    Consider using MultiLayerCalendarSystem.generate_agent_s_instruction() for better results.
    """
    if not all([title, date, time, duration]):
        return None

    instruction = f"Open Firefox, navigate to Google Calendar, and create an event titled '{title}' on {date.strftime('%B %d, %Y')} at {time.strftime('%I %M %p')}. The event will last for {duration}."
    if location:
        instruction += f" The location is {location}."
    instruction += " Confirm the event creation."
    return instruction

def smart_calendar_prompt(user_input: str):
    """
    NEW: Smart calendar event creation using the multi-layer system
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not set.")
        return False
    
    calendar_system = MultiLayerCalendarSystem(api_key)
    return calendar_system.create_calendar_event(user_input)

if __name__ == "__main__":
    print("🎯 Enhanced Prompt Engineer")
    print("Choose your method:")
    print("1. Legacy method (manual input)")
    print("2. Smart method (natural language)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        # Legacy method
        title, date, time, duration, location = get_event_details_from_user()
        if title and date and time and duration:
            agent_s_instruction = generate_agent_s_instruction(title, date, time, duration, location)
            if agent_s_instruction:
                create_calendar_event_with_agent_s(agent_s_instruction)
            else:
                print("Could not generate Agent-S instruction. Please provide all required details.")
        else:
            print("Event creation cancelled due to missing information.")
    
    elif choice == "2":
        # Smart method
        user_input = input("📅 Describe the calendar event you want to create: ")
        if user_input.strip():
            smart_calendar_prompt(user_input)
        else:
            print("Please provide a valid event description.")
    
    else:
        print("Invalid choice. Please run again and select 1 or 2.")
