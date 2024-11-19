import socket
import os
from cryptography.fernet import Fernet
from scapy.all import sniff, IP

SERVER_IP = '0.0.0.0'
SERVER_PORT = 61937
packet_no = 1
KEY = b"MTIzNDVhYmMxMjM0NWFiYzEyMzQ1YWJjMTIzNDVhYmM="
cipher = Fernet(KEY)

def send_encrypted_packet(packet_data):
    try:
        encrypted_data = cipher.encrypt(packet_data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(encrypted_data)
            encrypted_response = sock.recv(4096)
            response = cipher.decrypt(encrypted_response)
        return response
    except Exception as e:
        print(f"Error in send_encrypted_packet: {e}")
        return b''

def packet_handler(packet):
    global packet_no
    if IP in packet:
        packet_data = bytes(packet[IP])
        response = send_encrypted_packet(packet_data)
        if response:
            print(f"Recived packet no: {packet_no}")
            packet_no += 1

sniff(filter="ip", prn=packet_handler)
