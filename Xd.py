import socket
import colorama
import tkinter
import sys
import time
pc_name = socket.gethostname()

def menu():
    print(f"""
    
░░░░░████░░░░░░░░░░░░░░░████░░░░░
░░░░███░░░░░░░░░░░░░░░░░░░███░░░░
░░░███░░░░░░░░░░░░░░░░░░░░░███░░░
░░███░░░░░░░░░░░░░░░░░░░░░░░███░░
░███░░░░░░░░░░░░░░░░░░░░░░░░░███░
████░░░░░░░░░░░░░░░░░░░░░░░░░████
████░░░░░░░░░░░░░░░░░░░░░░░░░████
██████░░░░░░░███████░░░░░░░██████
█████████████████████████████████
█████████████████████████████████
░███████████████████████████████░
░░████░███████████████████░████░░
░░░░░░░███▀███████████▀███░░░░░░░
░░░░░░████──▀███████▀──████░░░░░░
░░░░░░█████───█████───█████░░░░░░
░░░░░░███████▄█████▄███████░░░░░░
░░░░░░░███████████████████░░░░░░░
░░░░░░░░█████████████████░░░░░░░░
░░░░░░░░░███████████████░░░░░░░░░
░░░░░░░░░░█████████████░░░░░░░░░░
░░░░░░░░░░░███████████░░░░░░░░░░░
░░░░░░░░░░███──▀▀▀──███░░░░░░░░░░
░░░░░░░░░░███─█████─███░░░░░░░░░░
░░░░░░░░░░░███─███─███░░░░░░░░░░░
░░░░░░░░░░░░█████████░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      Welcome {pc_name} 
1) Nitro G3N          
2) Roblox Cookie gen          
3) Your Ip          
https://github.com/SzaboJR         
https://discord.gg/Bamn4ChVya          
This just a template app!
Delete all of this if you want to!          
          """)

while True:
    menu()  # Megjelenítjük a menüt
    command = input(">")  # Kérjük be a felhasználó választását

    if command == "1":
        print("This is a template ")
        print("To have the nitro gen please download it at my github!")
        time.sleep(2)  # Adjunk egy kis szünetet, hogy a felhasználó el tudja olvasni az üzenetet
    elif command == "2":
        print("Roblox Cookie Generator option selected!")
        time.sleep(2)
    elif command == "3":
        print(f"Your IP is: {socket.gethostbyname(pc_name)}")
        time.sleep(2)
    else:
        print("Invalid option, please try again.")
