Files/project in progress.
# My Python Projects

This repository contains various Python projects that demonstrate the usage of different libraries and programming techniques. Each project is organized in its own Python file. The projects showcase different concepts such as GUI design, map generation, mathematical computations, text conversion, and more.

## Projects Overview

### 1. 🕒 Digital Watch with Alarm (`001_Digital watch.py`)
A simple digital clock that shows the current time and allows you to set an alarm. It uses the `tkinter` library for the GUI and displays the alarm message in the terminal when the set time is reached.

### 2. 🗺️ Search Location (`002_Search location.py`)
This project uses the `folium` and `geopy` libraries to search for a location and display it on a map. You input a location name, and it opens an interactive map showing the location on the web browser.

### 3. 🔺 Pascal's Triangle (`003_Pascal Triangle.py`)
Generates Pascal’s Triangle up to `N` rows, where `N` is provided by the user. The program demonstrates how to generate and print each row of Pascal's Triangle using Python.

### 4. 🟦🟨🟥 Romanian Flag (`004_Romanian Flag.py`)
This project uses the `matplotlib` library to draw the Romanian flag, consisting of blue, yellow, and red vertical stripes. It visually represents the Romanian national flag.

### 5. 📄➡️📝 Convert PDF to Word (`005_Convert PDF to Word.py`)
This script converts PDF files to Word documents. It uses the `PyPDF2` and `docx` libraries to extract text from the PDF and write it to a `.docx` file. The script also provides an option to search for PDF files in a specified directory.

### 6. 🌍📡🔍 IP Address Info (`006_IP Adress Info.py`)
Fetches information about an IP address (such as location, ISP, region, etc.) by using an external API (`ip-api.com`). You can input a target IP address or get your public IP automatically. 

### 7. 🔑🔐 Random Password Generator (`007_Random Password.py`)
Generates random passwords with specific complexity requirements. It ensures that the password contains at least 2 lowercase letters, 2 uppercase letters, 2 numbers, and 2 symbols.

### 8. 🛍️🏷️🛒 Online Shopping Store (`008_Online Shopping Store.py`)
A simple online shopping store with a menu where you can add products to the inventory, modify products, view products, and add them to your shopping cart. It allows customers to modify the quantity and price of products and finalize purchases.

---

## Technologies Used

- Python 3.x
- `tkinter` for GUI applications
- `folium` for map generation
- `geopy` for geolocation
- `PyPDF2` for PDF processing
- `docx` for Word document manipulation
- `colorama` and `termcolor` for colored text output
- `matplotlib` for visualizations
- `random`, `string`, and `os` for various utilities

---

## Getting Started

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/IulianSami/My_Projects.git

2. Make sure you have Python 3.x installed.

3. Install the necessary Python libraries using pip: 
   ```bash
    pip install -r requirements.txt

4. Run the specific project you want by executing the corresponding .py file.