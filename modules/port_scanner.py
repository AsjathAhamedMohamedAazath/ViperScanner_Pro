import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 3306: "MySQL",
    3389: "RDP", 8080: "HTTP-Alt"
}

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                try:
                    s.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
                    banner = s.recv(1024).decode(errors="ignore").strip()
                except:
                    banner = "No banner"
                service = COMMON_PORTS.get(port, "Unknown")
                return {"port": port, "service": service, "banner": banner}
    except Exception:
        return None

def run_port_scan(target, ports=range(1, 1025)):
    print("[*] Scanning ports...")
    open_ports = []
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Could not resolve target.")
        return []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)
        for res in results:
            if res:
                print(f"[+] Open: {res['port']}/tcp - {res['service']} - {res['banner'][:30]}")
                open_ports.append(res)
    return open_ports
