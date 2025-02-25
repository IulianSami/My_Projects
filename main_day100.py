


#TODO Workout

#TODO Digital watch

#1.  Digital watch :

# import tkinter as tk
# from time import strftime
#
# root = tk.Tk()
# root.title('Digital Clock')
#
# # Define the clock label
# clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
# clock_label.pack(anchor='center', fill='both', expand=True)
#
# # Function to update time
# def update_time():
#     current_time = strftime('%H:%M:%S')
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_time)  # Pass the function reference without parentheses
#
# update_time()
# root.mainloop()

#2.TODO:   CREATE MAP USING SEARCH PYTHON

# import folium
# from geopy.geocoders import Nominatim
# import webbrowser
# import os
#
# location_name = input('Enter a location:   ')
#
# geolocator = Nominatim(user_agent='geoapi')
# location = geolocator.geocode(location_name)
#
# if location:
#     # Create a map centered on user's location
#     latitude = location.latitude
#     longitude = location.longitude
#     clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)
#
#     marker = folium.Marker([latitude, longitude], popup=location_name)
#     marker.add_to(clcoding)
#
#     # Save the map to an HTML file and open it in the default web browser
#     map_file = 'location_map.html'
#     clcoding.save(map_file)
#     webbrowser.open('file://' + os.path.realpath(map_file))
# else:
#     print('Location not found. Please try again.')


# TODO 3: Python code for PASCAL's TRIANGLE

# def printPascal(N):
#     arr = [1]  # Initialize the first row
#     print("Pascal's triangle with", N, "rows:")
#
#     for i in range(N):
#         print("Row", i + 1, end=" : ")
#
#         # Print the current row
#         for val in arr:
#             print(val, end=" ")
#         print()  # Newline after each row
#
#         # Generate the next row
#         temp = [1]  # Start the next row with 1
#         for j in range(len(arr) - 1):
#             temp.append(arr[j] + arr[j + 1])  # Sum of adjacent elements
#         temp.append(1)  # End the row with 1
#         arr = temp  # Update the current row for the next iteration
#
#
# # Get user input and print Pascal's triangle
# N = int(input('Enter the number of rows for Pascal\'s triangle: '))
# printPascal(N)

# TODO 4: Myanmar flag using Python;

# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# import numpy as np
#
# fig, ax = plt.subplots(figsize=(8, 5))
# ax.fill_between([0, 3], 2, 3, color="#FED100")
# ax.fill_between([0, 3], 1, 2, color="#34B233")
# ax.fill_between([0, 3], 0, 1, color="#EA2839")
#
# def draw_star(center_x, center_y, radius, color, rotation_deg):
#     points = []
#     for i in range(10):
#         angle = (i * 36 + rotation_deg) * (np.pi / 180)
#         r = radius if i % 2 == 0 else radius / 2
#         x = center_x + r * np.cos(angle)
#         y = center_y + r * np.sin(angle)
#         points.append((x, y))
#     polygon = Polygon(points, closed=True, color=color)
#     ax.add_patch(polygon)
#
# draw_star(1.5, 1.5, 0.6, "white", rotation_deg=-55)
# ax.set_xlim(0, 3)
# ax.set_ylim(0, 3)
# ax.axis("off")
# plt.show()
# print("Happy independence Day Myanmar! ")

# TODO 5: Romania flag using Python;

# import matplotlib.pyplot as plt
#
# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(9, 5))
#
# # Define the width of each stripe
# stripe_width = 1 / 3
#
# # Draw the blue stripe (left)
# ax.fill_betweenx([0, 1], 0, stripe_width, color='#002B7F')  # Blue color
#
# # Draw the yellow stripe (center)
# ax.fill_betweenx([0, 1], stripe_width, 2 * stripe_width, color='#FCD116')  # Yellow color
#
# # Draw the red stripe (right)
# ax.fill_betweenx([0, 1], 2 * stripe_width, 1, color='#CE1126')  # Red color
#
# # Set limits and remove axes
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.axis('off')
#
# # Display the flag
# plt.title("La multi ani Romania!", fontsize=15)
# plt.show()


# TODO 6   CONVERSION PDF TO WORD # atentie unde cauta pdf ul si unde il salveaza C:
            # C: drop pdf here si il salveaza vezi info text

# import os
# import PyPDF2
# from docx import Document
#
#
# # Function to search for the PDF file using os.walk()
# def search_pdf_file(filename, start_dir="/"):
#     for root, dirs, files in os.walk(start_dir):
#         if filename in files:
#             return os.path.join(root, filename)
#     return None
#
#
# # Specify the filename you're searching for
# filename = "118567_6513eb3d888fa9.83734900.pdf"
#
# # Search for the PDF file in the specified directory (e.g., C:/ for Windows or / for Unix-like systems)
# pdf_path = search_pdf_file(filename, start_dir="C:/")  # Or "/" for Linux/Mac
#
# if pdf_path:
#     print(f"File found at: {pdf_path}")
#
#     # Create a new Word document
#     doc = Document()
#
#     # Open the found PDF file
#     with open(pdf_path, 'rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)
#
#         # Loop through each page of the PDF
#         for page in pdf_reader.pages:
#             text = page.extract_text()  # Extract text from each page
#
#             # If text is found, add it to the Word document as a paragraph
#             if text:
#                 doc.add_paragraph(text)
#             else:
#                 doc.add_paragraph("No text found on this page.")
#
#     # Save the Word document
#     word_filename = filename.replace('.pdf', '.docx')
#     doc.save(word_filename)
#     print(f"Conversion complete. The document is saved as '{word_filename}'.")
#
# else:
#     print("PDF file not found.")


# TODO 7:  Message  on whatssup using API:  in lucru

# import requests
#
# url = 'https://graph.facebook.com/v13.0/PHONE_NUMBER_ID/messages'
#
# headers = {
#     'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
#     'Content-Type': 'application/json'
# }
#
# data = {
#     "messaging_product": "Salutare py",
#     "to": "RECIPIENT_PHONE_NUMBER", "+40740372392" # Include country code, e.g., +1234567890
#     "text": {
#         "body": "Hello from Python using WhatsApp API!"
#     }
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# if response.status_code == 200:
#     print("Message sent successfully!")
# else:
#     print(f"Failed to send message. Status code: {response.status_code}")
#
#
#




