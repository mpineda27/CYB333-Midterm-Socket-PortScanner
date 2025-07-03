# CYB333-Midterm-Socket-PortScanner

## Project Overview
This project demonstrates socket communication and a port scanner implementation in Python, with additional documentation and reflection on security automation practices.

## Objectives
- Build a simple socket communication tool (server/client).
- Create a Python-based port scanner for localhost or scanme.nmap.org.
- Document use of Jupyter Notebooks for data analysis and visualization.
- Practice DevSecOps principles in coding, testing, and documentation.

## How to Run
1. Clone this repository.
2. Install dependencies (see requirements.txt if present).
3. Run the Python scripts as described in the main report.
4. Refer to Jupyter Notebook screenshots for data analysis examples.

## Dependencies
- Python 3.9+
- Standard Python libraries (`socket`, `os`, etc.)
- [psutil] (if used)
- Jupyter Notebook (for `.ipynb` files and screenshots)

## Screenshots
See the following files:
- `jupyter_bar_chart.png`
- `jupyter_df_example.png`
- `jupyter_line_plot.png`
- `Jupyter_Notebook_Screenshot.png`

## AI Tools Used
GitHub Copilot and ChatGPT were used for code suggestions, documentation, and troubleshooting.

## Contact
Michael Pineda - mpineda27

## Final Course Project Report

The full project report can be found here: [Revised CourseProject_Pineda.docx](./Revised%20CourseProject_Pineda.docx)

# Automated Log Monitoring and Alerting System

## Project Overview
This project implements a scalable, robust, and secure log monitoring and alerting tool in Python. It automatically detects security-relevant events (e.g., failed logins, privilege escalations) in system logs using pattern matching and regular expressions, and sends real-time alerts to security teams via multiple channels.

## Objectives
- Monitor system log files in real time for security-relevant events.
- Automatically detect and alert on suspicious activity using regex pattern matching.
- Send notifications via email and/or file-based alerts.
- Support cross-platform use (Windows and Linux).
- Enable customization through configuration files.

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt` (requirements file to be added if needed).
3. Edit the configuration file (`config.yaml` or `.env`) for alerting channels, log file paths, and regex patterns.
4. Run `python log_monitor.py` to start monitoring.
5. Check screenshots for sample outputs and see Jupyter Notebooks for code analysis and documentation.

## Dependencies
- Python 3.9+
- `watchdog` (for file system monitoring)
- `re` (regular expressions, standard Python)
- `smtplib` (standard Python, for email notifications)
- `pyyaml` (if using YAML config)
- Jupyter Notebook (for analysis and demonstration)

## Files in this Repository
- `log_monitor.py` — main monitoring script.
- `config.yaml` or `.env` — configuration file.
- `alerting.py` — notification module (if split).
- `notebooks/` — Jupyter Notebooks for documentation and analysis.
- `screenshots/` — Demo screenshots showing alerts and outputs.
- `Revised CourseProject_Pineda.docx` — Full project write-up.

## AI Tools Used
ChatGPT and GitHub Copilot were used for brainstorming, code generation, debugging, and best practices review.

## Screenshots
See the `/screenshots` folder and linked images below for example outputs and running code.

## Final Course Project Report
The full report can be found here: [Revised CourseProject_Pineda.docx](./Revised%20CourseProject_Pineda.docx)

## Contact
Michael Pineda - mpineda27

# Automated Log Monitoring and Alerting System

## Project Overview
This project implements a real-time, automated log monitoring and alerting tool in Python. It is designed to detect security-relevant events (such as repeated failed logins or privilege escalations) by automatically scanning system logs, matching patterns, and sending timely alerts to security teams via file and email notifications. The project showcases security automation, modular programming, robust error handling, and AI-assisted development.

## Objectives
- Continuously monitor specified system log files for security-relevant events.
- Use efficient event-driven mechanisms to react to log changes (using `watchdog`).
- Match patterns using regular expressions for flexible detection.
- Support multiple alerting channels (file, email).
- Provide easy configuration for deployment.
- Follow secure coding best practices.

## How to Run
1. Clone this repository.
2. Install dependencies:  
   `pip install watchdog`
3. Configure `config.json` (if used) or update `log_monitor.py` with your settings (log path, alerting options, email credentials).
4. Run `log_monitor.py`.
5. Review alerts in designated files or your email.

## Dependencies
- Python 3.9+
- [watchdog](https://pypi.org/project/watchdog/)
- `re` (standard library)
- `smtplib` (standard library)

## Screenshots
See `/screenshots` for demonstration of running log monitor, sample alerts, and Jupyter data analysis.

## AI Tools Used
ChatGPT was used for code troubleshooting, design ideas, and error handling. GitHub Copilot helped with autocomplete and code snippets for handling edge cases, notifications, and modular development.

## Author
Michael Pineda (mpineda27)

## Final Course Project Report
See [Revised_CourseProject_Pineda.docx](Revised_CourseProject_Pineda.docx)

