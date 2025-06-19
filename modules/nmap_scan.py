import subprocess
import shutil

def is_nmap_installed():
    return shutil.which("nmap") is not None

def run_nmap_scan(target, output_file="nmap_output.txt"):
    if not is_nmap_installed():
        print("[-] Nmap is not installed or not in PATH.")
        return None

    print("[*] Running Nmap service & vuln scan...")
    try:
        cmd = [
            "nmap", "-sV", "--script=vulners", "-T4", "-Pn", "-oN", output_file, target
        ]
        subprocess.run(cmd, check=True)
        with open(output_file, "r", encoding="utf-8") as f:
            return f.read()
    except subprocess.CalledProcessError:
        print("[-] Nmap scan failed.")
        return None
