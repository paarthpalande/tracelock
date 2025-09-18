# TRACELOCK

> Securing Your Data, Securing Your Future...

TRACELOCK is a simple, colorized log analysis tool for Linux/Windows text logs. It scans log files for common security-related events (authentication failures, session open/close, kernel messages, warnings, service start/stop, etc.) and prints color-coded matches to make triage faster.

---

## Features

* Parse Linux and Windows (text-exported) logs
* Categories: authentication failures, session alerts, connections, kernel/system logs, service start/stop, warnings, and more
* Colorized terminal output for quick visual triage (requires `colorama`)
* Menu-driven, non-recursive interface for easier navigation
* Safe handling of empty results and file errors

---

## Author

**Parth Palande**

---

## Requirements

* Python 3.8+
* `pyfiglet` (for banner)
* `colorama` (for colored output)

Install dependencies with pip:

```bash
pip install pyfiglet colorama
```

---

## Installation

1. Clone the repo or copy `tracelock.py` to your machine.
2. Ensure the script is executable or invoke with Python:

```bash
python3 tracelock.py
```

> Notes: Many system logs in `/var/log/` require root privileges. Instead of running the script as `sudo`, it's often safer to export the needed portion of a system log to a file you own (e.g., `sudo journalctl -u ssh -n 500 --no-pager > ~/ssh_journal.txt`) and run TRACELOCK against that file.

---

## Usage

Run the script and follow the interactive menu:

```bash
python3 tracelock.py
```

1. Choose **Linux Log** or **Windows Log**.
2. Provide the path to a text log file (e.g., `/var/log/auth.log` or `~/ssh_journal.txt`).
3. Pick a category from the menu to view matches (colorized output).

### Quick test

Create a small test log and run TRACELOCK:

```bash
cat > ~/tracelock_test.log <<'EOF'
Sep 18 09:15:23 kali sshd[1223]: authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.1.50
Sep 18 09:20:45 kali systemd[1]: session opened for user kali by (uid=0)
Sep 18 09:30:11 kali kernel: usb 1-1: device descriptor read/64, error -71
EOF

python3 tracelock.py
# Choose Linux Log, then enter: /home/<you>/tracelock_test.log
```

---

## Sample output

(TRACELOCK prints category headers, a count of matches, and the matching log lines colorized. See the repository examples or run the test above.)

---

## Exporting journalctl output

If your system uses systemd, you can export logs to a file and analyze them with TRACELOCK:

```bash
sudo journalctl -n 500 --no-pager > ~/system_journal.txt
python3 tracelock.py
# enter: /home/<you>/system_journal.txt
```

---

## Contributing

Contributions, improvements to regexes, or additional parsing logic are welcome. Please open issues or pull requests on GitHub.

---

## License

Choose a license for your project (e.g., MIT). If you want, add a `LICENSE` file. Example snippet for MIT:

```
MIT License

Copyright (c) <year> Parth Palande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
```

---

## Publishing to GitHub (quick commands)

If you haven’t already initialized a git repo, here’s a minimal workflow:

```bash
git init
git add tracelock.py README.md
git commit -m "Initial commit: TRACELOCK log analyzer"
# create a repository on GitHub (via web) then add remote, for example:
git remote add origin git@github.com:YOUR_USERNAME/tracelock.git
git branch -M main
git push -u origin main
```

---

## Contact

For questions or help, open an issue in the repository or contact the author: Parth Palande.

---

Happy logging! 🎯
