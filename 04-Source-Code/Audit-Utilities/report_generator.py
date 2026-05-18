#!/usr/bin/env python3
"""
================================================================================
AUTOMATED VULNERABILITY AUDIT & SYSTEM REPORTING ENGINE
================================================================================
File:        report_generator.py
Description: Compiles raw network scan results into structured, professional
             audit logs and remediation roadmaps.
================================================================================
"""

import os
import sys
from datetime import datetime

class AuditReporter:
    def __init__(self, target_host: str, output_directory: str = "."):
        self.target_host = target_host
        self.output_directory = output_directory
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        self.findings = []
        
    def add_finding(self, service: str, port: int, banner: str, risk_level: str, fix: str) -> None:
        """Appends a verified system vulnerability finding to the report inventory."""
        self.findings.append({
            "service": service,
            "port": port,
            "banner": banner,
            "risk": risk_level.upper(),
            "remediation": fix
        })
        print(f"    [+] Logged [{risk_level.upper()}] finding on port {port} ({service})")

    def compile_report(self) -> str:
        """Generates a professional Markdown audit summary report file."""
        report_filename = f"Audit_Report_{self.target_host.replace('.', '_')}_{self.timestamp}.md"
        report_path = os.path.join(self.output_directory, report_filename)
        
        markdown_content = f"""# 🛡️ AUTOMATED SYSTEM SECURITY AUDIT REPORT
**Target Host/IP:** {self.target_host}  
**Audit Timestamp:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Assessor Signature:** ReconTrapper Security Automated Engine  

---

## 📊 EXECUTIVE SUMMARY
This automated assessment evaluates the exposed attack surface of the target host. A total of **{len(self.findings)}** notable service configurations or potential vulnerabilities were identified during the discovery cycle.

## 🔍 DETAILED AUDIT FINDINGS
"""
        if not self.findings:
            markdown_content += "\n### ✅ No high-risk open service exposures or vulnerabilities detected.\n"
        else:
            for idx, item in enumerate(self.findings, 1):
                markdown_content += f"""
### Finding {idx}: {item['service']} Service Exposure (Port {item['port']}/TCP)
* **Risk Classification Level:** `{item['risk']}`
* **Detected Software Banner:** `{item['banner']}`
* **Technical Impact Assessment:** Unencrypted or outdated system banners expose software versions to potential network reconnaissance mapping.
* **🔧 Core Remediation Steps:** {item['remediation']}
--------------------------------------------------------------------------------
"""
                
        markdown_content += "\n\n*End of automated audit documentation. Keep this file restricted to authorized system administrators only.*\n"
        
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        return report_path

if __name__ == "__main__":
    print("=" * 80)
    print(" 🛠️  AUTOMATED SECURITY REPORT GENERATOR INITIALIZED")
    print("=" * 80)
    
    # Prompt the user interactively for the host details to simulate compile operations
    target = input("[?] Enter the Target Host IP/Name evaluated: ").strip()
    if not target:
        target = "10.0.2.4"
        
    reporter = AuditReporter(target)
    
    print(f"\n[*] Compiling mock dataset to demonstrate engine layout for host: {target}")
    # Populate the generator with common sandbox vulnerabilities to demonstrate how it builds out reports
    reporter.add_finding("FTP (vsftpd)", 21, "vsftpd 2.3.4", "High", "Update vsftpd engine immediately to patch backdoors. Disable anonymous FTP access tokens.")
    reporter.add_finding("SSH (OpenSSH)", 22, "OpenSSH 4.7p1 Debian 8ubuntu1", "Medium", "Enforce strong public-key cryptographic authentication and disable root passwords logins.")
    reporter.add_finding("HTTP (Apache)", 80, "Apache/2.2.8 (Ubuntu) DAV/2", "Low", "Modify the httpd.conf file configuration to set 'ServerTokens Prod' and hide specific version info.")
    
    try:
        final_path = reporter.compile_report()
        print("\n" + "=" * 80)
        print(f" 🎉 REPORT GENERATION COMPLETE!")
        print(f" 👉 Destination Path: {final_path}")
        print("=" * 80)
    except Exception as e:
        print(f"[❌] Error compiling report file: {e}")
