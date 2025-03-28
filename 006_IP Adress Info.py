#6.  🌍📡🔍  IP Adress Information Using Python:

#Without VPN  

import urllib.request as urllib2
import json

def get_public_ip():
    """Get the user's public IP using an online service."""
    try:
        response = urllib2.urlopen("https://api64.ipify.org?format=json")
        data = json.loads(response.read().decode("utf-8"))
        return data["ip"]
    except Exception as e:
        print(f"Could not retrieve public IP: {e}")
        return None

while True:
    ip = input("What is your target IP (or type 'my' to get your own IP): ").strip()

    # If the user enters 'my', automatically retrieve the public IP
    if ip.lower() == "my":
        ip = get_public_ip()
        if ip:
            print(f"Your public IP is: {ip}")
        else:
            print("Could not determine your public IP.")
            continue

    # Check if the user entered a valid IP
    if not ip:
        print("Please enter a valid IP address.")
        continue

    url = f"http://ip-api.com/json/{ip}"

    try:
        response = urllib2.urlopen(url)
        data = response.read()
        values = json.loads(data)

        # Check if the API returned success
        if values.get("status") == "success":
            print("\n🌍 IP Information:")
            print(f"📍 IP: {values.get('query', 'N/A')}")
            print(f"🏙️ City: {values.get('city', 'N/A')}")
            print(f"🗺️ Country: {values.get('country', 'N/A')}")
            print(f"📡 ISP: {values.get('isp', 'N/A')}")
            print(f"🌎 Region: {values.get('regionName', 'N/A')}")
            print(f"⏰ Timezone: {values.get('timezone', 'N/A')}\n")
        else:
            print(f"❌ Error: {values.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

    break  # Stop execution after a single run
