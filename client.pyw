import socket
import os
import sys
from typing import NoReturn

def handle_command(command: str) -> str:
    if command == 'status':
        return "I'm alive!"
    elif command == 'turn_off':
        if sys.platform == "win32":
            os.system('shutdown /s /t 1')
        else:
            os.system('shutdown -h now')
        return "Turning off..."

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 50000))
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    if data := conn.recv(1024):
                        response = handle_command(data.decode())
                        conn.sendall(response.encode())
                    else:
                        break
        except Exception as e:
            print(f"An error occurred: {e}")
