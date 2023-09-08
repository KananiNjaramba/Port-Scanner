# A simple Port Scanner to check for open ports on a computer. In Cyber Security Open ports pose a security risk and closing unnecesarry ports is good security practise.
# A project by Kanani Njaramba in fulfillment of EBU Python course requirements
import csv
import socket
import matplotlib.pyplot as plt

# Initialize counters for open and closed ports
open_ports = 0
closed_ports = 0

# Lists to store open and closed port details
open_port_details = []
closed_port_details = []

# Open the CSV file
with open('server_list.csv', 'r') as csv_file:# Input the file path of the csv file with ports and IP addresses
    csv_reader = csv.DictReader(csv_file)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        host = row['host']
        port = int(row['port'])  # Convert port to an integer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((host, port))
        
        if result == 0:
            print(f"Connected to {host}:{port}")
            open_ports += 1
            open_port_details.append((host, port))
        else:
            print(f"Failed to connect to {host}:{port}")
            closed_ports += 1
            closed_port_details.append((host, port))
        
        s.close()

# Export open and closed port details to CSV files
with open('open_ports.csv', 'w', newline='') as open_file:
    open_writer = csv.writer(open_file)
    open_writer.writerow(['Host', 'Port'])
    open_writer.writerows(open_port_details)

with open('closed_ports.csv', 'w', newline='') as closed_file:
    closed_writer = csv.writer(closed_file)
    closed_writer.writerow(['Host', 'Port'])
    closed_writer.writerows(closed_port_details)

# Create a pie chart to visualize open vs. closed ports
labels = 'Open Ports', 'Closed Ports'
sizes = [open_ports, closed_ports]
colors = ['green', 'red']
explode = (0.1, 0)  # Explode the first slice (Open Ports)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()