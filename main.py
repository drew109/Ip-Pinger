import os

def ping(ip, count, fast):
    if fast:
        options = "-c 1 -i 0.2"  # Send 1 request with a 0.2 second interval between pings
    else:
        options = "-c 1"  # Send 1 request with the default interval between pings
    for i in range(count):
        response = os.system("ping " + options + " " + ip)
        if response == 0:
            print(ip + " is up!")
        else:
            print(ip + " is down.")

# Test the function by prompting the user for the number of pings to send and whether to use a fast ping rate
ip = "Your IP"
count = int(input("Enter the number of pings to send: "))
fast = input("Use a fast ping rate (y/n)? ").lower() == "y"
ping(ip, count, fast)
