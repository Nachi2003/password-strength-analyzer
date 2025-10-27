import tkinter as tk
from tkinter import ttk
import zxcvbn

def check_password_strength(event=None):
    """
    Gets password from entry, analyzes it, and updates the UI.
    This function is now triggered by key releases.
    """
    password = password_entry.get()
    
    # Clear previous results
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    
    if not password:
        # --- Handle empty password ---
        result_text.insert(tk.END, "Please enter a password.", "error")
        result_text.config(state=tk.DISABLED)
        # Reset progress bar
        progressbar['value'] = 0
        progressbar.config(style="Horizontal.TProgressbar") # Reset to default style
        return

    # --- Analysis ---
    results = zxcvbn.zxcvbn(password)
    score = results.get('score')
    crack_time = results.get('crack_times_display', {}).get('offline_slow_hashing_1e4_per_second', 'N/A')
    warning = results.get('feedback', {}).get('warning', '')
    suggestions = results.get('feedback', {}).get('suggestions', [])
    
    # --- Display Results ---
    
    # 1. Score Text
    strength_map = {
        0: ("❌ Very Weak", "red"),
        1: ("🔥 Weak", "orange"),
        2: ("⚠️ Fair", "darkgoldenrod"),
        3: ("✅ Good", "blue"),
        4: ("💪 Strong", "green")
    }
    score_text, score_color = strength_map.get(score, ("Unknown", "black"))
    result_text.insert(tk.END, f"Strength: {score_text}\n", score_color)
    
    # 2. Update Progress Bar
    # Map score (0-4) to a value (20-100) and a style
    progress_map = {
        0: (20, "red.Horizontal.TProgressbar"),
        1: (40, "orange.Horizontal.TProgressbar"),
        2: (60, "darkgoldenrod.Horizontal.TProgressbar"),
        3: (80, "blue.Horizontal.TProgressbar"),
        4: (100, "green.Horizontal.TProgressbar")
    }
    progress_value, progress_style = progress_map.get(score, (0, "Horizontal.TProgressbar"))
    
    progressbar['value'] = progress_value
    progressbar.config(style=progress_style)
    
    # 3. Crack Time
    result_text.insert(tk.END, f"Est. Crack Time: {crack_time}\n\n", "default")
    
    # 4. Warning
    if warning:
        result_text.insert(tk.END, "Warning:\n", "warning")
        result_text.insert(tk.END, f"{warning}\n\n", "default")
    
    # 5. Suggestions
    if suggestions:
        result_text.insert(tk.END, "Suggestions:\n", "info")
        for suggestion in suggestions:
            result_text.insert(tk.END, f"  - {suggestion}\n", "default")
            
    result_text.config(state=tk.DISABLED)

# --- Set up the main window ---
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x370") # Made window a little taller

# --- Configure styles ---
style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11, "bold"))
style.configure("TEntry", font=("Arial", 11))

# --- NEW: Define custom progress bar colors ---
# We create a new style for each color
style.configure("red.Horizontal.TProgressbar", troughcolor='#f2f2f2', background='#d9534f')
style.configure("orange.Horizontal.TProgressbar", troughcolor='#f2f2f2', background='#f0ad4e')
style.configure("darkgoldenrod.Horizontal.TProgressbar", troughcolor='#f2f2f2', background='#b58900')
style.configure("blue.Horizontal.TProgressbar", troughcolor='#f2f2f2', background='#0275d8')
style.configure("green.Horizontal.TProgressbar", troughcolor='#f2f2f2', background='#5cb85c')

# --- Create widgets ---
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

prompt_label = ttk.Label(main_frame, text="Enter a password to analyze:")
prompt_label.pack(pady=5)

password_entry = ttk.Entry(main_frame, show="*")
password_entry.pack(fill=tk.X, pady=5, ipady=4)

# --- NEW: Add the Progress Bar ---
progressbar = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=100, mode='determinate', value=0)
progressbar.pack(fill=tk.X, pady=5)

# (We'll keep the button, but it's optional now)
analyze_button = ttk.Button(main_frame, text="Analyze Strength", command=check_password_strength)
# analyze_button.pack(pady=10) # You can uncomment this if you still want the button

# --- Create the result text area ---
result_text = tk.Text(main_frame, height=10, wrap=tk.WORD, font=("Arial", 10))
result_text.pack(fill=tk.BOTH, expand=True, pady=(10,0))

# Define text colors
result_text.tag_configure("red", foreground="#d9534f")
result_text.tag_configure("orange", foreground="#f0ad4e")
result_text.tag_configure("darkgoldenrod", foreground="#b58900")
result_text.tag_configure("blue", foreground="#0275d8")
result_text.tag_configure("green", foreground="#5cb85c")
result_text.tag_configure("warning", font=("Arial", 10, "bold"), foreground="#d9534f")
result_text.tag_configure("info", font=("Arial", 10, "bold"), foreground="#0275d8")
result_text.tag_configure("default", foreground="black")
result_text.tag_configure("error", foreground="red", font=("Arial", 10, "italic"))

result_text.insert(tk.END, "Results will appear here as you type.", "default")
result_text.config(state=tk.DISABLED)

# --- NEW: Bind key release to the analysis function ---
# <KeyRelease> triggers the event *after* the key is let go
password_entry.bind("<KeyRelease>", check_password_strength)

# Bind the "Enter" key to the button click (still works)
root.bind('<Return>', lambda event: analyze_button.invoke())

# --- Run the app ---
root.mainloop()