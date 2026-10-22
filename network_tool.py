
import socket
from datetime import datetime

# Display the tool title
print("=== Network Information Tool ===")

# Display current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", current_time)

# Display your computer's hostname
computer_name = socket.gethostname()
print("Your computer's hostname:", computer_name)

# Ask for a domain name
domain = input("\nEnter a domain name (e.g. google.com): ").strip()

if not domain:
    print("Error: Please enter a domain name.")

else:
    try:
        # Find the IP address
        ip_address = socket.gethostbyname(domain)

        # Display the results
        print("\n" + "=" * 40)
        print("=== Investigation Results ===")
        print("Domain name:", domain)
        print("IP address:", ip_address)
        print("=" * 40)

    except socket.gaierror:
        print("\nError: Could not find the IP address.")
        print("Check the domain name or your internet connection.")
