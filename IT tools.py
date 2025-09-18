import shutil
import psutil
import subprocess

# --- Function 1: Disk Usage ---
def check_disk_usage(path="C:\\"):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    print(f"\nDisk usage on {path}: {percent_used:.2f}%")
    if percent_used > 80:
        print("⚠️ Warning: Disk space is above 80%")
    else:
        print("✅ Disk space is OK")

# --- Function 2: Memory Usage ---
def check_memory_usage():
    memory = psutil.virtual_memory()
    percent_used = memory.percent
    print(f"\nMemory usage: {percent_used}%")
    if percent_used > 80:
        print("⚠️ High memory usage")
    else:
        print("✅ Memory usage is OK")

# --- Function 3: CPU Usage ---
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=2)
    print(f"\nCPU usage: {cpu_percent}%")
    if cpu_percent > 80:
        print("⚠️ High CPU usage")
    else:
        print("✅ CPU usage is OK")

# --- Function 4: Ping Test ---
def ping_test(host="8.8.8.8"):
    print(f"\nPinging {host}...")
    try:
        output = subprocess.check_output(
            ["ping", host, "-n", "4"],  # -n 4 = 4 pings on Windows
            universal_newlines=True
        )
        print(output)
    except subprocess.CalledProcessError:
        print("❌ Ping failed")

# --- Toolkit Menu ---
def main():
    while True:
        print("\n--- IT Support Toolkit ---")
        print("1. Check Disk Usage")
        print("2. Check Memory Usage")
        print("3. Check CPU Usage")
        print("4. Ping Test")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            check_disk_usage()
        elif choice == "2":
            check_memory_usage()
        elif choice == "3":
            check_cpu_usage()
        elif choice == "4":
            ping_test()
        elif choice == "5":
            print("Exiting toolkit...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
