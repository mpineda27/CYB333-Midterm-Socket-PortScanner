"""
log_monitor.py

Automated Log Monitoring and Alerting System
Author: Michael Pineda
"""

import time
import re
import smtplib
import os
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ========== CONFIGURATION ==========
LOG_FILE_PATH = '/var/log/auth.log'  # Change this to the log file you want to monitor
PATTERN = r'Failed password|sudo:|authentication failure'  # Regex for security events
ALERT_EMAIL = os.environ.get("ALERT_EMAIL")    # Set these in your environment for security!
ALERT_PASS = os.environ.get("ALERT_PASS")
ALERT_TO = os.environ.get("ALERT_TO")
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# ========== ALERTING FUNCTION ==========
def send_email_alert(event_line):
    """Send email alert for detected security event."""
    if not ALERT_EMAIL or not ALERT_PASS or not ALERT_TO:
        print("Email credentials or recipient not set in environment variables.")
        return
    msg = MIMEText(f"Security Event Detected:\n{event_line}")
    msg['Subject'] = 'Automated Log Alert'
    msg['From'] = ALERT_EMAIL
    msg['To'] = ALERT_TO
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(ALERT_EMAIL, ALERT_PASS)
        server.sendmail(ALERT_EMAIL, ALERT_TO, msg.as_string())
        server.quit()
        print("Alert sent via email.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# ========== FILE MONITORING ==========
class LogEventHandler(FileSystemEventHandler):
    def __init__(self, logfile, pattern):
        self.logfile = logfile
        self.pattern = re.compile(pattern)
        self.position = 0

    def on_modified(self, event):
        if event.src_path == self.logfile:
            with open(self.logfile, 'r') as f:
                f.seek(self.position)
                new_lines = f.readlines()
                self.position = f.tell()
            for line in new_lines:
                if self.pattern.search(line):
                    print(f"Security event detected: {line.strip()}")
                    send_email_alert(line.strip())

def monitor_log_file():
    print(f"Monitoring {LOG_FILE_PATH} for security events...")
    event_handler = LogEventHandler(LOG_FILE_PATH, PATTERN)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH) or '.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_log_file()

