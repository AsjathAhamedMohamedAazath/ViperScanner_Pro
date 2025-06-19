from datetime import datetime
import html

def generate_html_report(target, whois_data, ports, tech_info, output_path, nmap_output=None):
    html_content = f"""
    <html>
    <head>
        <title>ViperScan Pro Report - {target}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0e1117;
                color: #e5e5e5;
                padding: 20px;
                overflow-x: hidden;
            }}
            h1, h2 {{
                color: #00ffff;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
                word-break: break-word;
                table-layout: fixed;
            }}
            th, td {{
                border: 1px solid #444;
                padding: 10px;
                text-align: left;
                overflow-wrap: break-word;
                word-wrap: break-word;
            }}
            th {{
                background-color: #1f2937;
            }}
            td {{
                background-color: #111827;
            }}
            code, pre {{
                white-space: pre-wrap;
                word-wrap: break-word;
                overflow-x: auto;
                display: block;
                background-color: #1a1a1a;
                padding: 10px;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <h1>ViperScan Pro Report</h1>
        <p><strong>Target:</strong> {html.escape(target)}</p>
        <p><strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

        <h2>📡 WHOIS & DNS Info</h2>
        <pre>{html.escape(str(whois_data))}</pre>

        <h2>🧠 Open Ports</h2>
        <table>
            <tr><th>Port</th><th>Service</th><th>Banner</th></tr>
            {''.join(f"<tr><td>{p['port']}</td><td>{html.escape(p['service'])}</td><td>{html.escape(p['banner'])}</td></tr>" for p in ports)}
        </table>

        <h2>🌐 HTTP Technology Fingerprint</h2>
        <pre>{html.escape(str(tech_info))}</pre>

        <h2>🧪 Nmap Scan Results</h2>
        <pre>{html.escape(nmap_output) if nmap_output else "Nmap not run or not installed."}</pre>
    </body>
    </html>
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
