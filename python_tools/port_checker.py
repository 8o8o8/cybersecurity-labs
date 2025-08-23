import socket

def check_port(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2) # timeout in seconds
        result = sock.connect_ex((host, port))
        sock.close()

        if result == 0:
            print(f"✅ Port {port} is OPEN on {host}")
        else:
            print(f"❌ Port {port} is CLOSED on {host}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    host = input("Enter a hostname or IP (example: google.com): ")
    ports = [80, 443, 22, 3389] # you can add more ports here

    for port in ports:
        check_port(host, port)