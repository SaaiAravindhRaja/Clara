"""
GUI Version of Multi-Layer Calendar System
Provides a user-friendly interface for calendar event creation
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import os
from dotenv import load_dotenv
from multi_layer_prompt_system import MultiLayerCalendarSystem

# Load environment variables from .env file
load_dotenv()

class CalendarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 AI Calendar Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize the calendar system
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            messagebox.showerror("Error", "OPENAI_API_KEY environment variable not set!")
            return
            
        self.calendar_system = MultiLayerCalendarSystem(api_key)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🎯 AI Calendar Assistant", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Tell me what calendar event you'd like to create, and I'll handle the rest!",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            input_frame, 
            text="📝 Describe your event:", 
            font=("Arial", 12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor=tk.W)
        
        self.input_text = tk.Text(
            input_frame, 
            height=3, 
            font=("Arial", 11),
            wrap=tk.WORD,
            relief=tk.RAISED,
            borderwidth=2
        )
        self.input_text.pack(fill=tk.X, pady=(5, 10))
        
        # Example text
        example_text = "Example: 'Create a diving event on August 22nd at 8am'"
        self.input_text.insert(tk.END, example_text)
        self.input_text.bind("<FocusIn>", self.clear_placeholder)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.create_button = tk.Button(
            button_frame,
            text="🚀 Create Event",
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            command=self.create_event_threaded
        )
        self.create_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_button = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Arial", 12),
            bg='#95a5a6',
            fg='white',
            relief=tk.RAISED,
            borderwidth=2,
            command=self.clear_input
        )
        self.clear_button.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            self.root, 
            mode='indeterminate',
            length=300
        )
        self.progress.pack(pady=10)
        
        # Output frame
        output_frame = tk.Frame(self.root, bg='#f0f0f0')
        output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(
            output_frame, 
            text="📊 System Output:", 
            font=("Arial", 12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            font=("Consolas", 10),
            bg='#2c3e50',
            fg='#ecf0f1',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to create calendar events!")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#34495e',
            fg='white',
            font=("Arial", 10)
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def clear_placeholder(self, event):
        """Clear placeholder text when user clicks on input"""
        current_text = self.input_text.get("1.0", tk.END).strip()
        if "Example:" in current_text:
            self.input_text.delete("1.0", tk.END)
            
    def clear_input(self):
        """Clear the input text"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.status_var.set("Ready to create calendar events!")
        
    def log_output(self, message):
        """Add message to output text area"""
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)
        self.root.update_idletasks()
        
    def create_event_threaded(self):
        """Run event creation in a separate thread to prevent UI freezing"""
        user_input = self.input_text.get("1.0", tk.END).strip()
        
        if not user_input or "Example:" in user_input:
            messagebox.showwarning("Warning", "Please enter a valid event description!")
            return
            
        # Disable button and start progress
        self.create_button.config(state=tk.DISABLED)
        self.progress.start()
        self.status_var.set("Processing your request...")
        self.output_text.delete("1.0", tk.END)
        
        # Run in separate thread
        thread = threading.Thread(target=self.create_event, args=(user_input,))
        thread.daemon = True
        thread.start()
        
    def create_event(self, user_input):
        """Create calendar event (runs in separate thread)"""
        try:
            self.log_output(f"🎯 Processing request: {user_input}")
            self.log_output("=" * 50)
            
            # Redirect the calendar system output to our GUI
            import sys
            from io import StringIO
            
            # Capture stdout
            old_stdout = sys.stdout
            sys.stdout = captured_output = StringIO()
            
            try:
                success = self.calendar_system.create_calendar_event(user_input)
                
                # Get captured output
                output = captured_output.getvalue()
                sys.stdout = old_stdout
                
                # Display output in GUI
                for line in output.split('\n'):
                    if line.strip():
                        self.log_output(line)
                
                if success:
                    self.status_var.set("✅ Event created successfully!")
                    messagebox.showinfo("Success", "Calendar event created successfully!")
                else:
                    self.status_var.set("❌ Event creation failed")
                    messagebox.showerror("Error", "Failed to create calendar event. Check the output for details.")
                    
            except Exception as e:
                sys.stdout = old_stdout
                self.log_output(f"❌ Error: {str(e)}")
                self.status_var.set("❌ Error occurred")
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
                
        finally:
            # Re-enable button and stop progress
            self.root.after(0, self.reset_ui)
            
    def reset_ui(self):
        """Reset UI elements after operation completes"""
        self.create_button.config(state=tk.NORMAL)
        self.progress.stop()

def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = CalendarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()