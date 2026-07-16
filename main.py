
from analyzer import LogAnalyzer
from pathlib import Path

print("=== Welcome to System Log Analyzer ===")

while True:
    user_path = input("Enter the path to your log file (e.g., system_logs.txt): ")
    
    path = Path(user_path)

    if path.exists() and path.is_file():
        break
    else:
        print("Path doesn't exist or is not a file. Enter a valid path!")


analyzer = LogAnalyzer(user_path)

while True:
    print("\nMenu:")
    print("1. Display all log entries")
    print("2. Filter the bugs")
    print("3. Quit")

    choice = input("Select an option (1-3): ")
    
    if choice == "1":
        print(f"\nFile content: ({analyzer.source}):")
        analyzer.showEverything()
        
    elif choice == "2":
        output_file = input("Input your desired file name (e.g., warnings.txt): ")
        print("\nList of exceptions:")
        analyzer.filterWarnings(output_file)

    elif choice == "3":
        print("Built by rawlogic")
        break
    else:
        print("Wrong choice. Try again.")