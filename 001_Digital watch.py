#1. 🕒   Digital watch with alarm :

import tkinter as tk
from time import strftime
import threading
import time
from termcolor import colored  

# Fereastra pentru ceas
root = tk.Tk()
root.title('Digital Clock with Alarm')

# Eticheta pentru ceas
clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
clock_label.pack(anchor='center', fill='both', expand=True)

# Variabila care va ține ora alarmei
alarm_time = None

# Funcția care actualizează timpul pe ceas
def update_time():
    current_time = strftime('%H:%M:%S')  # Obține ora curentă
    clock_label.config(text=current_time)  # Actualizează ceasul

    # Verifică dacă ora curentă corespunde cu ora alarmei
    if alarm_time and current_time[:5] == alarm_time:
        print(colored(f"A sunat alarma la {alarm_time}!", 'red'))  # Afișează mesajul roșu în consolă
        
    clock_label.after(1000, update_time)  # Actualizează ceasul la fiecare secundă

# Funcția pentru setarea alarmei
def set_alarm():
    global alarm_time
    alarm_input = input("Setează ora alarmei (format HH:MM): ")

    try:
        # Verifică dacă inputul este într-un format corect
        time.strptime(alarm_input, '%H:%M')  # Verifică dacă formatul e corect
        alarm_time = alarm_input  # Salvează ora alarmei
        print(f"Alarma este setată la: {alarm_time}")
    except ValueError:
        print("Format invalid. Te rog să introduci ora în formatul HH:MM.")

# Setează alarma într-un thread separat
def alarm_thread_function():
    while True:
        set_alarm()
        time.sleep(1)  # Evită blocarea programului

# Pornește funcția de actualizare a timpului și setarea alarmei în paralel
thread = threading.Thread(target=alarm_thread_function)
thread.daemon = True
thread.start()

update_time()

root.mainloop()