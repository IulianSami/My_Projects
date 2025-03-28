#1. 🕒   Digital watch with alarm :

import tkinter as tk
from time import strftime
import threading
import time
from termcolor import colored  

# Window for the clock
root = tk.Tk()
root.title('Digital Clock with Alarm')

# Label for the clock
clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
clock_label.pack(anchor='center', fill='both', expand=True)

# Variable to store the alarm time
alarm_time = None

# Function to update the time on the clock
def update_time():
    current_time = strftime('%H:%M:%S')  # Get the current time
    clock_label.config(text=current_time)  # Update the clock

    # Check if the current time matches the alarm time
    if alarm_time and current_time[:5] == alarm_time:
        print(colored(f"Alarm rang at {alarm_time}!", 'red'))  # Display the message in red in the console
        
    clock_label.after(1000, update_time)  # Update the clock every second

# Function to set the alarm
def set_alarm():
    global alarm_time
    alarm_input = input("Set the alarm time (format HH:MM): ")

    try:
        # Check if the input is in the correct format
        time.strptime(alarm_input, '%H:%M')  # Verify if the format is correct
        alarm_time = alarm_input  # Save the alarm time
        print(f"Alarm is set for: {alarm_time}")
    except ValueError:
        print("Invalid format. Please enter the time in HH:MM format.")

# Set the alarm in a separate thread
def alarm_thread_function():
    while True:
        set_alarm()
        time.sleep(1)  # Prevents program blocking

# Start the time update function and alarm setting in parallel
thread = threading.Thread(target=alarm_thread_function)
thread.daemon = True
thread.start()

update_time()

root.mainloop()