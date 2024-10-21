import os
import hashlib

print("\033[92m░██████╗░██████╗░███████╗███████╗███╗░░██╗        ██╗░░░░░██╗░█████╗░███╗░░██╗\033[0m")
print("\033[92m██╔════╝░██╔══██╗██╔════╝██╔════╝████╗░██║        ██║░░░░░██║██╔══██╗████╗░██║\033[0m")
print("\033[92m██║░░██╗░██████╔╝█████╗░░█████╗░░██╔██╗██║        ██║░░░░░██║██║░░██║██╔██╗██║\033[0m")
print("\033[92m██║░░╚██╗██╔══██╗██╔══╝░░██╔══╝░░██║╚████║        ██║░░░░░██║██║░░██║██║╚████║\033[0m")
print("\033[92m╚██████╔╝██║░░██║███████╗███████╗██║░╚███║        ███████╗██║╚█████╔╝██║░╚███║\033[0m")
print("\033[92m░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝        ╚══════╝╚═╝░╚════╝░╚═╝░░╚══╝\033[0m")
print("\033[92m                                       By: Masar                              \033[0m")
# A dictionary of known malicious file hashes for simplicity (MD5 format)
known_malicious_hashes = {
    "5d41402abc4b2a76b9719d911017c592": "Malware A",
    "098f6bcd4621d373cade4e832627b4f6": "Malware B",
}

# A list of known suspicious file names
suspicious_file_names = [
    "malware.exe",
    "virus.bat",
    "trojan.txt",
    "keylogger.py",
]

def get_file_md5(file_path):
    """Calculate the MD5 hash of a file."""
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        return file_hash
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_file(file_path):
    """Scan a file for known malware signatures."""
    file_hash = get_file_md5(file_path)
    if file_hash in known_malicious_hashes:
        print(f"[ALERT] Malware detected: {known_malicious_hashes[file_hash]} in {file_path}")
        return True
    elif os.path.basename(file_path) in suspicious_file_names:
        print(f"[WARNING] Suspicious file name detected: {file_path}")
        return True
    else:
        print(f"[SAFE] {file_path} is clean.")
        return False

def scan_directory(directory):
    """Scan a directory for malicious files."""
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            scan_file(file_path)
    print("Scan completed.")

def delete_file_by_name(directory, target_name):
    """Delete a file by its name."""
    found = False
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name == target_name:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                found = True
    if not found:
        print(f"No file named {target_name} found in {directory}.")

def find_file_by_name(directory, target_name):
    """Find a file by its name."""
    found = False
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name == target_name:
                file_path = os.path.join(root, file_name)
                print(f"Found: {file_path}")
                found = True
    if not found:
        print(f"No file named {target_name} found in {directory}.")

def main():
    print("╔Choose a function:")
    print("║╔1. Antivirus Scan")
    print("║║2. Delete File by Name")
    print("╚╚3. Find File by Name")
    choice = input("Enter the number of your choice: ")

    directory = input("Enter the directory path: ")

    if choice == "1":
        scan_directory(directory)
    elif choice == "2":
        target_name = input("Enter the file name to delete: ")
        delete_file_by_name(directory, target_name)
    elif choice == "3":
        target_name = input("Enter the file name to find: ")
        find_file_by_name(directory, target_name)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
