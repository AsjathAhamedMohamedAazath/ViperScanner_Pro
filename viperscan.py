import argparse
from modules.port_scanner import run_port_scan
from modules.http_fingerprint import detect_technologies
from modules.whois_lookup import get_domain_info
from modules.report_generator import generate_html_report
from modules.nmap_scan import run_nmap_scan, is_nmap_installed
import os
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="ViperScan Pro - Advanced Recon and Scanning Tool")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP address")
    parser.add_argument("--full", action="store_true", help="Run full scan with all modules")
    parser.add_argument("-o", "--output", help="Save HTML report to file")
    args = parser.parse_args()

    target = args.target
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    print(f"\n[+] Starting ViperScan Pro on: {target}\n")

    # 1. WHOIS and Domain Info
    whois_data = get_domain_info(target)

    # 2. Port Scanning
    open_ports = run_port_scan(target)

    # 3. HTTP(S) Fingerprinting
    tech_info = detect_technologies(target)

    # 4. Optional Nmap Scan
    nmap_output = None
    if is_nmap_installed():
        nmap_output = run_nmap_scan(target)

    # 5. Report Generation
    if args.output:
        output_path = args.output
    else:
        output_path = f"reports/scan-{target.replace('.', '_')}-{timestamp}.html"
        os.makedirs("reports", exist_ok=True)

    generate_html_report(target, whois_data, open_ports, tech_info, output_path, nmap_output)

    print(f"\n[✓] Scan completed. Report saved to: {output_path}\n")


if __name__ == "__main__":
    main()
