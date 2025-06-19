import httpx

def detect_technologies(target):
    urls = [f"http://{target}", f"https://{target}"]
    tech_info = {}

    for url in urls:
        try:
            response = httpx.get(url, timeout=5, follow_redirects=True)
            tech_info["url"] = str(response.url)
            tech_info["status_code"] = response.status_code
            tech_info["headers"] = dict(response.headers)

            # Simple tech detection based on headers
            server = response.headers.get("server", "Unknown")
            powered_by = response.headers.get("x-powered-by", "Unknown")
            tech_info["server"] = server
            tech_info["powered_by"] = powered_by
            print(f"[+] HTTP Response from {url} - Server: {server}, Powered By: {powered_by}")
            break  # Use first successful response
        except Exception as e:
            continue

    if not tech_info:
        print("[-] HTTP fingerprinting failed on all URLs.")

    return tech_info
