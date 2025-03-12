# # My_Python_Projects

#1.    Digital watch :

# import tkinter as tk
# from time import strftime

# root = tk.Tk()
# root.title('Digital Clock')

# # Define the clock label
# clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
# clock_label.pack(anchor='center', fill='both', expand=True)

# # Function to update time
# def update_time():
#     current_time = strftime('%H:%M:%S')
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_time)  # Pass the function reference without parentheses

# update_time()
# root.mainloop()

# print("&" * 20)


#2:    Create map / search location using  Python:

# import folium
# from geopy.geocoders import Nominatim
# import webbrowser
# import os

# location_name = input('Enter a location:   ')

# geolocator = Nominatim(user_agent='geoapi')
# location = geolocator.geocode(location_name)

# if location:
#     # Create a map centered on user's location
#     latitude = location.latitude
#     longitude = location.longitude
#     clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

#     marker = folium.Marker([latitude, longitude], popup=location_name)
#     marker.add_to(clcoding)

#     # Save the map to an HTML file and open it in the default web browser
#     map_file = 'location_map.html'
#     clcoding.save(map_file)
#     webbrowser.open('file://' + os.path.realpath(map_file))
# else:
#     print('Location not found. Please try again.')

# print("&" * 20)


#3:    Python code for PASCAL's TRIANGLE:

# def printPascal(N):
#     arr = [1]  # Initialize the first row
#     print("Pascal's triangle with", N, "rows:")

#     for i in range(N):
#         print("Row", i + 1, end=" : ")

#         # Print the current row
#         for val in arr:
#             print(val, end=" ")
#         print()  # Newline after each row

#         # Generate the next row
#         temp = [1]  # Start the next row with 1
#         for j in range(len(arr) - 1):
#             temp.append(arr[j] + arr[j + 1])  # Sum of adjacent elements
#         temp.append(1)  # End the row with 1
#         arr = temp  # Update the current row for the next iteration


# # Get user input and print Pascal's triangle
# N = int(input('Enter the number of rows for Pascal\'s triangle: '))
# printPascal(N)

# print("&" * 20)


#4:    Myanmar flag using Python:

# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# import numpy as np

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.fill_between([0, 3], 2, 3, color="#FED100")
# ax.fill_between([0, 3], 1, 2, color="#34B233")
# ax.fill_between([0, 3], 0, 1, color="#EA2839")

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

# draw_star(1.5, 1.5, 0.6, "white", rotation_deg=-55)
# ax.set_xlim(0, 3)
# ax.set_ylim(0, 3)
# ax.axis("off")
# plt.show()
# print("Happy independence Day Myanmar! ")

# print("&" * 20)


#5:    Romanian flag using Python:

# import matplotlib.pyplot as plt

# # Create a figure and axis
# fig, ax = plt.subplots(figsize=(9, 5))

# # Define the width of each stripe
# stripe_width = 1 / 3

# # Draw the blue stripe (left)
# ax.fill_betweenx([0, 1], 0, stripe_width, color='#002B7F')  # Blue color

# # Draw the yellow stripe (center)
# ax.fill_betweenx([0, 1], stripe_width, 2 * stripe_width, color='#FCD116')  # Yellow color

# # Draw the red stripe (right)
# ax.fill_betweenx([0, 1], 2 * stripe_width, 1, color='#CE1126')  # Red color

# # Set limits and remove axes
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.axis('off')

# # Display the flag
# plt.title("La multi ani Romania!", fontsize=15)
# plt.show()

# print("&" * 20)

#6.    CONVERSION PDF TO WORD


# import os
# import PyPDF2
# from docx import Document


# # Function to search for the PDF file using os.walk()
# def search_pdf_file(filename, start_dir="/"):
#     for root, dirs, files in os.walk(start_dir):
#         if filename in files:
#             return os.path.join(root, filename)
#     return None


# # Specify the filename you're searching for
# filename = "118567_6513eb3d888fa9.83734900.pdf"

# # Search for the PDF file in the specified directory (e.g., C:/ for Windows or / for Unix-like systems)
# pdf_path = search_pdf_file(filename, start_dir="C:/")  # Or "/" for Linux/Mac

# if pdf_path:
#     print(f"File found at: {pdf_path}")

#     # Create a new Word document
#     doc = Document()

#     # Open the found PDF file
#     with open(pdf_path, 'rb') as pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Loop through each page of the PDF
#         for page in pdf_reader.pages:
#             text = page.extract_text()  # Extract text from each page

#             # If text is found, add it to the Word document as a paragraph
#             if text:
#                 doc.add_paragraph(text)
#             else:
#                 doc.add_paragraph("No text found on this page.")

#     # Save the Word document
#     word_filename = filename.replace('.pdf', '.docx')
#     doc.save(word_filename)
#     print(f"Conversion complete. The document is saved as '{word_filename}'.")

# else:
#     print("PDF file not found.")

# print("&" * 20)



#7.    IP Adress Information Using Python:

# Without VPN  

# import urllib.request as urllib2
# import json

# def get_public_ip():
#     """Obține IP-ul public al utilizatorului folosind un serviciu online."""
#     try:
#         response = urllib2.urlopen("https://api64.ipify.org?format=json")
#         data = json.loads(response.read().decode("utf-8"))
#         return data["ip"]
#     except Exception as e:
#         print(f"Could not retrieve public IP: {e}")
#         return None

# while True:
#     ip = input("What is your target IP (or type 'my' to get your own IP): ").strip()

#     # Dacă utilizatorul introduce 'my', află IP-ul public automat
#     if ip.lower() == "my":
#         ip = get_public_ip()
#         if ip:
#             print(f"Your public IP is: {ip}")
#         else:
#             print("Could not determine your public IP.")
#             continue

#     # Verificăm dacă utilizatorul a introdus un IP valid
#     if not ip:
#         print("Please enter a valid IP address.")
#         continue

#     url = f"http://ip-api.com/json/{ip}"

#     try:
#         response = urllib2.urlopen(url)
#         data = response.read()
#         values = json.loads(data)

#         # Verificăm dacă API-ul a returnat succes
#         if values.get("status") == "success":
#             print("\n🌍 IP Information:")
#             print(f"📍 IP: {values.get('query', 'N/A')}")
#             print(f"🏙️ City: {values.get('city', 'N/A')}")
#             print(f"🗺️ Country: {values.get('country', 'N/A')}")
#             print(f"📡 ISP: {values.get('isp', 'N/A')}")
#             print(f"🌎 Region: {values.get('regionName', 'N/A')}")
#             print(f"⏰ Timezone: {values.get('timezone', 'N/A')}\n")
#         else:
#             print(f"❌ Error: {values.get('message', 'Unknown error')}")

#     except Exception as e:
#         print(f"⚠️ An error occurred: {e}")

#     break  # Oprește execuția după o singură rulare

# print("&" * 20)

#8.    Random Password Generated Using Python:

# import random

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()_-+=?><[]"

# all_chars = lower + upper + numbers + symbols
# lenght = int(input("Please enter password lenght: "))

# password = "".join(random.sample(all_chars, lenght))
# print("Generated password: ", password)


# print("&" * 20)


#9.  Meniu magazin cu introducere articole in inventar si cumparare.
  
# --------------------------------------
#           Meniu Magazin
# --------------------------------------
# 1. Vizualizează produse
# 2. Adaugă produs în coș
# 3. Vizualizează coșul
# 4. Finalizează comanda
# 5. Ieși
# --------------------------------------
# Alege o opțiune: 


from colorama import init, Fore, Style

# Inițializare colorama
init(autoreset=True)

# Lista de produse disponibile cu stoc
products = {
    "Laptop": {"price": 3000, "stock": 10},
    "Telefon": {"price": 1500, "stock": 15},
    "Căști": {"price": 300, "stock": 50},
    "Televizor": {"price": 2500, "stock": 5},
    "Mouse": {"price": 150, "stock": 20},
}

# Coșul de cumpărături (inițial gol)
cart = {}

# Funcția pentru a arăta produsele disponibile
def show_products():
    print(Fore.GREEN + "\nProduse disponibile:")
    for index, (product, info) in enumerate(products.items(), start=1):
        print(Fore.YELLOW + f"{index}. {product} - {info['price']} RON (Stoc: {info['stock']})")

# Funcția pentru a adăuga produse în coș
def add_to_cart():
    show_products()
    try:
        choice = int(input(Fore.YELLOW + "\nAlege numărul produsului pentru a-l adăuga în coș: "))
        if 1 <= choice <= len(products):
            product_name = list(products.keys())[choice - 1]
            quantity = int(input(Fore.YELLOW + f"Câte {product_name} vrei să adaugi în coș? "))

            # Verificăm dacă există suficiente produse în stoc
            if quantity <= products[product_name]["stock"]:
                if product_name in cart:
                    cart[product_name] += quantity
                else:
                    cart[product_name] = quantity

                # Scădem cantitatea din stoc
                products[product_name]["stock"] -= quantity
                print(Fore.GREEN + f"Produsul {product_name} a fost adăugat în coș!")
            else:
                print(Fore.RED + f"Nu sunt suficiente produse în stoc pentru {product_name}. Mai sunt doar {products[product_name]['stock']} disponibile.")
        else:
            print(Fore.RED + "Opțiune invalidă.")
    except ValueError:
        print(Fore.RED + "Te rog să introduci un număr valid.")

# Funcția pentru a vizualiza coșul de cumpărături
def view_cart():
    if cart:
        print(Fore.GREEN + "\nCoșul tău de cumpărături:")
        total_price = 0
        for product, quantity in cart.items():
            price = products[product]["price"]
            total_price += price * quantity
            print(Fore.YELLOW + f"{product} - {quantity} x {price} RON")
        print(Fore.YELLOW + f"\nTotal: {total_price} RON")
    else:
        print(Fore.RED + "Coșul tău este gol.")

# Funcția pentru a finaliza comanda
def checkout():
    if cart:
        print(Fore.GREEN + "\nMulțumim pentru cumpărături!")
        total_price = 0
        for product, quantity in cart.items():
            price = products[product]["price"]
            total_price += price * quantity
            print(Fore.YELLOW + f"{product} - {quantity} x {price} RON")
        print(Fore.YELLOW + f"\nTotal de plată: {total_price} RON")

        # Golește coșul după ce comanda este finalizată
        cart.clear()
        print(Fore.GREEN + "\nComanda a fost finalizată. La revedere!")
    else:
        print(Fore.RED + "Coșul este gol. Nu poți finaliza comanda fără produse.")

# Funcția care arată meniul principal
def show_menu():
    print(Fore.YELLOW + "\n--------------------------------------")
    print(Fore.YELLOW + "          Meniu Magazin")
    print(Fore.YELLOW + "--------------------------------------")
    print(Fore.GREEN + "1. Vizualizează produse")
    print(Fore.GREEN + "2. Adaugă produs în coș")
    print(Fore.GREEN + "3. Vizualizează coșul")
    print(Fore.GREEN + "4. Finalizează comanda")
    print(Fore.GREEN + "5. Ieși")
    print(Fore.YELLOW + "--------------------------------------")

# Funcția principală
def main():
    while True:
        show_menu()

        try:
            option = int(input(Fore.YELLOW + "Alege o opțiune: "))

            if option == 1:
                show_products()
            elif option == 2:
                add_to_cart()
            elif option == 3:
                view_cart()
            elif option == 4:
                checkout()
                break  # După ce finalizăm comanda, ieșim din aplicație

            elif option == 5:
                print(Fore.GREEN + "Ieșire din aplicație. La revedere!")
                break
            else:
                print(Fore.RED + "Opțiune invalidă. Te rog să alegi 1, 2, 3, 4 sau 5.")
        except ValueError:
            print(Fore.RED + "Te rog să introduci un număr valid.\n")

# Rulează aplicația
if __name__ == "__main__":
    main()