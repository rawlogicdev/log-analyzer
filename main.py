with open("system_logs.txt", "r", encoding="utf-8") as file:
    linie = file.readlines()
print(f"Liczba wpisów w logach: {len(linie)}")

while True:
    print("\nMenu:")
    print("1. Wyświetl wszystkie wpisy")
    print("2. Wyfiltruj linie z błędem")
    print("3. Zakończ program")

    choice = input("Wybierz opcję (1-3): ")
    if choice == "1":
        print("\nZawartość logów:")
        for line in linie:
            print(line.strip())
    elif choice == "2":
        print("\nWpisy z błędem:")
        with open("critical_logs.txt", "a", encoding="utf-8") as log_file:
            for line in linie:
                if "ERROR" in line or "WARNING" in line or "CRITICAL" in line:
                    stripped_line = line.strip()
                    print(stripped_line)
                    log_file.write(stripped_line + "\n")

    elif choice == "3":
        print("Zakończono program.")
        break
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")