import socket
import whois

def get_domain_info(target):
    data = {}
    try:
        ip = socket.gethostbyname(target)
        data["ip"] = ip
        data["dns"] = socket.gethostbyaddr(ip)[0]
        print(f"[+] DNS Resolved: {target} → {ip}")
    except Exception:
        data["ip"] = "Unknown"
        data["dns"] = "Lookup failed"

    try:
        w = whois.whois(target)
        data["whois"] = {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "emails": w.emails
        }
        print(f"[+] WHOIS Lookup: Domain - {w.domain_name}, Registrar - {w.registrar}")
    except Exception as e:
        data["whois"] = "WHOIS lookup failed"

    return data
