import re
import pyfiglet
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# ----------------- INTRO -----------------
def intro():
    styled_text = pyfiglet.figlet_format('TRACELOCK', font='slant')
    print(Fore.CYAN + styled_text)
    print(Fore.MAGENTA + "\t> by Parth Palande | Securing Your Data, Securing Your Future...\n")

# ----------------- HELPER -----------------
def display_logs(title, pattern, content, color=Fore.WHITE):
    """Find and display logs matching a regex pattern with colors."""
    refine = re.findall(pattern, content, re.MULTILINE)
    count = len(refine)

    print(Fore.CYAN + f"[*] {title}")
    print(Fore.GREEN + f"\t* Number of logs: {count}")
    print("-" * (len(refine[0]) + 10 if count > 0 else 20))

    if count > 0:
        for log in refine:
            print(color + log)
    else:
        print(Fore.RED + "No logs found.")

    print()

# ----------------- LINUX FUNCTIONS -----------------
def auth_failure(content):
    pattern = r"(authentication\s+failure.+|Kerberos\s+authentication\s+failed|Authentication\s+failed\s+from.+|Couldn't\sauthenticate.+)"
    display_logs("AUTHENTICATION FAILURE LOGS :-", pattern, content, Fore.RED)

def session_alerts(content):
    pattern = r"(session\s+opened.+|session\s+closed.+|ALERT.+)"
    display_logs("SESSION OPENED/CLOSED/LOGROTATE ALERT :-", pattern, content, Fore.YELLOW)

def connection(content):
    pattern = r"(connection\s+from.+|timed\s+out.+)"
    display_logs("CONNECTION FROM USERS :-", pattern, content, Fore.BLUE)

def start_stop_restart(content):
    pattern = r"(shutdown.+|startup.+|syslogd.+|Starting.+|started)"
    display_logs("START/SHUTDOWN/RESTART :-", pattern, content, Fore.GREEN)

def auto_detect(content):
    pattern = r"(Auto-detected.+|\*+\s+info\s+\[.+)"
    display_logs("AUTO-DETECTION LOGS :-", pattern, content, Fore.CYAN)

def login(content):
    pattern = r"(LOGIN\s+ON.+)"
    display_logs("LOGIN USERS :-", pattern, content, Fore.MAGENTA)

def operations(content):
    pattern = r"(removing\s+device.+|creating\s+device.+)"
    display_logs("CREATING/REMOVING DEVICE NODES :-", pattern, content, Fore.YELLOW)

def warnings(content):
    pattern = r"(notify\s+question.+|endpoint.+|warning:.+)"
    display_logs("NOTIFY QUESTION/ENDPOINTS/WARNINGS :-", pattern, content, Fore.RED)

def system_logs(content):
    pattern = r"(kernel:.+|random:.+|network:.+)"
    display_logs("KERNEL/RANDOM/NETWORK LOGS :-", pattern, content, Fore.CYAN)

# ----------------- WINDOWS FUNCTIONS -----------------
def load(content):
    pattern = r"(Loaded.+)"
    display_logs("LOADED SERVICE LOGS :-", pattern, content, Fore.GREEN)

def init(content):
    pattern = r"(Scavenge:.+|Ending.+|Starting.+|service\s+starts\s+successfully.+|Startup.+|No\s+startup\s+processing\s+required.+)"
    display_logs("INITIALIZE LOGS :-", pattern, content, Fore.CYAN)

def sqm(content):
    pattern = r"(SQM:.+)"
    display_logs("SOFTWARE QUALITY METRICS(SQM) LOGS :-", pattern, content, Fore.MAGENTA)

def session(content):
    pattern = r"(Session:.+|Failed\s+to\s+internally\s+open\s+package.+|Read\s+out\s+cached\s+package.+)"
    display_logs("SESSION LOGS :-", pattern, content, Fore.BLUE)

def warning_window(content):
    pattern = r"(Warning:.+|Expecting\s+attribute\s+name.+|Failed\s+to\s+get\s+next\s+element.+)"
    display_logs("WARNING/EXPECTING/FAILED LOGS :-", pattern, content, Fore.RED)

def loading(content):
    pattern = r"(Loading\s+offline\s+registry.+|Unloading\s+offline\s+registry.+|Offline\s+image\s+is:.+|manifest\s+caching.+)"
    display_logs("LOADING/UNLOADING OFFLINE REGISTRY LOGS :-", pattern, content, Fore.YELLOW)

# ----------------- MENUS -----------------
def linux_menu(content):
    while True:
        print(Fore.CYAN + "[*] LINUX OPTIONS :-")
        print("\t[1.] AUTHENTICATION FAILURE LOG.")
        print("\t[2.] SESSION OPENED/CLOSED/LOGROTATE ALERT LOG.")
        print("\t[3.] CONNECTION FROM USERS LOG.")
        print("\t[4.] START/SHUTDOWN/RESTART LOG.")
        print("\t[5.] AUTO-DETECTION LOG.")
        print("\t[6.] LOGIN USERS LOG.")
        print("\t[7.] CREATING/REMOVING DEVICE NODES LOG.")
        print("\t[8.] NOTIFY QUESTION/ENDPOINTS/WARNINGS LOG.")
        print("\t[9.] KERNEL/RANDOM/NETWORK LOG.")
        print("\t[10.] ALL OF THE ABOVE.")
        print("\t[11.] BACK TO MAIN MENU.")
        print("\t[12.] EXIT.\n")

        choice = input(Fore.YELLOW + "[+] Enter your choice: ")

        if choice == "1": auth_failure(content)
        elif choice == "2": session_alerts(content)
        elif choice == "3": connection(content)
        elif choice == "4": start_stop_restart(content)
        elif choice == "5": auto_detect(content)
        elif choice == "6": login(content)
        elif choice == "7": operations(content)
        elif choice == "8": warnings(content)
        elif choice == "9": system_logs(content)
        elif choice == "10":
            auth_failure(content); session_alerts(content); connection(content)
            start_stop_restart(content); auto_detect(content); login(content)
            operations(content); warnings(content); system_logs(content)
        elif choice == "11": return
        elif choice == "12":
            print(Fore.GREEN + "\nThank you for choosing TRACELOCK. Your trust is our priority!\n")
            sys.exit(0)

def windows_menu(content):
    while True:
        print(Fore.CYAN + "[*] WINDOWS OPTIONS :-")
        print("\t[1.] LOADED SERVICE LOG.")
        print("\t[2.] INITIALIZE LOG.")
        print("\t[3.] SOFTWARE QUALITY METRICS(SQM) LOG.")
        print("\t[4.] SESSION LOG.")
        print("\t[5.] WARNING/EXPECTING/FAILED LOG.")
        print("\t[6.] LOADING/UNLOADING OFFLINE REGISTRY LOG.")
        print("\t[7.] ALL OF THE ABOVE.")
        print("\t[8.] BACK TO MAIN MENU.")
        print("\t[9.] EXIT.\n")

        choice = input(Fore.YELLOW + "[+] Enter your choice: ")

        if choice == "1": load(content)
        elif choice == "2": init(content)
        elif choice == "3": sqm(content)
        elif choice == "4": session(content)
        elif choice == "5": warning_window(content)
        elif choice == "6": loading(content)
        elif choice == "7":
            load(content); init(content); sqm(content)
            session(content); warning_window(content); loading(content)
        elif choice == "8": return
        elif choice == "9":
            print(Fore.GREEN + "\nThank you for choosing TRACELOCK. Your trust is our priority!\n")
            sys.exit(0)

# ----------------- MAIN MENU -----------------
def option():
    while True:
        print(Fore.CYAN + "[*] OPTIONS :-")
        print("\t[1.] Linux Log.")
        print("\t[2.] Windows Log.")
        print("\t[3.] Exit.\n")

        choice = input(Fore.YELLOW + "[+] Choose your Option: ")

        if choice == "1":
            filename = input(Fore.YELLOW + "[+] Enter Name of Linux Log File: ")
            try:
                with open(filename, "r") as f:
                    content = f.read()
                linux_menu(content)
            except FileNotFoundError:
                print(Fore.RED + "[!] File not found. Try again.\n")

        elif choice == "2":
            filename = input(Fore.YELLOW + "[+] Enter Name of Windows Log File: ")
            try:
                with open(filename, "r") as f:
                    content = f.read()
                windows_menu(content)
            except FileNotFoundError:
                print(Fore.RED + "[!] File not found. Try again.\n")

        elif choice == "3":
            print(Fore.GREEN + "\nThank you for choosing TRACELOCK. Your trust is our priority!\n")
            sys.exit(0)

# ----------------- RUN -----------------
if __name__ == "__main__":
    intro()
    option()
