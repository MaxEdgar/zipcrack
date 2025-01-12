import zipfile
import sys
import time
import os
import random
import string

# ANSI escape codes for green color
GREEN = '\033[32m'
RESET = '\033[0m'

# Function to extract ZIP with a given password
def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode('utf-8'))
        return True
    except:
        return False

# Function for brute-forcing ZIP passwords
def brute_force_zip(zip_file_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_file_path)
    except FileNotFoundError:
        print(f"{GREEN}[!] ZIP file not found!{RESET}")
        return
    except zipfile.BadZipFile:
        print(f"{GREEN}[!] Invalid ZIP file format!{RESET}")
        return

    try:
        with open(wordlist_path, 'r') as wordlist:
            for line in wordlist:
                password = line.strip()
                print(f"{GREEN}[*] Trying: {password}{RESET}")
                if extract_zip(zip_file, password):
                    print(f"{GREEN}[+] Password found: {password}{RESET}")
                    return
    except FileNotFoundError:
        print(f"{GREEN}[!] Wordlist file not found!{RESET}")
        return

    print(f"{GREEN}[-] Password not found in the wordlist :((.{RESET}")

# Experimental password generator
def generate_passwords():
    length = int(input(f"{GREEN}[*] Enter password length: {RESET}"))
    filename = "pass.txt"

    # Ask whether to replace or append
    if os.path.exists(filename):
        print(f"{GREEN}[!] '{filename}' already exists.{RESET}")
        option = input(f"{GREEN}[*] Replace (R) or Append (A)? {RESET}").lower()
        if option == 'r':  # Replace
            mode = 'w'
            print(f"{GREEN}[!] Replacing the old password list.{RESET}")
        elif option == 'a':  # Append
            mode = 'a'
            print(f"{GREEN}[+] Appending to the existing list.{RESET}")
        else:
            print(f"{GREEN}[!] Invalid option! Returning to menu.{RESET}")
            return
    else:
        mode = 'w'

    # Generate passwords
    chars = string.ascii_letters + string.digits + string.punctuation
    with open(filename, mode) as f:
        for _ in range(1000):  # Generate 1000 passwords
            password = ''.join(random.choice(chars) for _ in range(length))
            f.write(password + '\n')

    print(f"{GREEN}[+] 1000 passwords saved to '{filename}'{RESET}")
    print(f"{GREEN}[EXPERIMENTAL] Use with caution!{RESET}")

# Display directory in a grid format
def list_directory():
    print(f"{GREEN}+{'-' * 40}+")  # Grid border
    print(f"{GREEN}| Current Directory: {os.getcwd()} |")
    print(f"{GREEN}+{'-' * 40}+")
    
    files = os.listdir()
    columns = 4  # Number of columns in the grid
    for i, file in enumerate(files):
        print(f"{GREEN}{file:<20}", end="")
        if (i + 1) % columns == 0:  # New row after 4 columns
            print()
    print("\n" + f"{GREEN}+{'-' * 40}+")

# Display the banner
def display_banner():
    print(f"{GREEN}+{'-' * 40}+")
    print(f"{GREEN}|{' ' * 40}|")

    # Display name with colors
    print(f"{GREEN}|{' Maxmilliano'}{GREEN} Edgar{' ♥'}{GREEN}      |")

    print(f"{GREEN}|{' ' * 40}|")
    print(f"{GREEN}+{'-' * 40}+")

# Main Menu
def main_menu():
    while True:
        os.system('clear')  # Clears the screen
        display_banner()
        print(f"{GREEN}[1] Brute Force ZIP Password{RESET}")
        print(f"{GREEN}[2] Exit{RESET}")
        print(f"{GREEN}[3] Help{RESET}")
        print(f"{GREEN}[4] Credits{RESET}")
        print(f"{GREEN}[5] Password Generator [EXPERIMENTAL]{RESET}")
        print(f"{GREEN}-{'-' * 40}")

        choice = input(f"{GREEN}[*] Enter your choice: {RESET}")

        if choice == '1':
            list_directory()
            zip_file_path = input(f"{GREEN}[*] Enter ZIP file path: {RESET}")
            wordlist_path = input(f"{GREEN}[*] Enter wordlist path: {RESET}")
            start_time = time.time()
            brute_force_zip(zip_file_path, wordlist_path)
            end_time = time.time()
            print(f"{GREEN}[*] Elapsed time: {end_time - start_time:.2f} seconds{RESET}")
            input(f"\n{GREEN}Press Enter to continue...{RESET}")
        elif choice == '2':
            print(f"{GREEN}Goodbye! ♥{RESET}")
            sys.exit(0)
        elif choice == '3':
            print(f"{GREEN}\n[HELP]{RESET}")
            print(f"{GREEN}1. Place the ZIP file and wordlist in the same directory or provide full paths.{RESET}")
            print(f"{GREEN}2. Select option 1 and enter file paths when prompted.{RESET}")
            print(f"{GREEN}3. The tool will try each password in the wordlist and extract if successful.{RESET}")
            print(f"{GREEN}4. Use option 5 to generate passwords for testing purposes.{RESET}")
            input(f"\n{GREEN}Press Enter to return to the menu...{RESET}")
        elif choice == '4':
            print(f"{GREEN}\n[CREDITS]{RESET}")
            print(f"{GREEN}Created by Maxmilliano Edgar ♥{RESET}")
            print(f"{GREEN}For educational purposes only!{RESET}")
            input(f"\n{GREEN}Press Enter to return to the menu...{RESET}")
        elif choice == '5':
            generate_passwords()
            input(f"\n{GREEN}Press Enter to return to the menu...{RESET}")
        else:
            print(f"{GREEN}[!] Invalid choice! Try again.{RESET}")

# Entry point
if __name__ == "__main__":
    os.system('clear')  # Clears the terminal for a clean interface
    main_menu()
