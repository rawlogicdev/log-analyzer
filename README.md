````markdown
🇬🇧

# Simple LogAnalyzer 📋🔍

[![Version](https://img.shields.io/badge/version-2.1-blue.svg)](https://github.com/rawlogicdev/simple-loganalyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, modular, and terminal-based utility designed to parse, filter, and extract critical error logs from messy log files. This tool can be used either as an **interactive CLI tool** or imported as an **OOP library** in other Python projects.

---

## 🌟 Key Features

- **OOP Architecture:** Clean object-oriented structure using Python classes, making it easily reusable.
- **Advanced Target Directory Management:** User defines both the source file path and a dedicated target output directory where logs will be securely exported.
- **Smart Parsing Algorithm:** Analyzes the first 4 words of each log entry, automatically strips punctuation, and matches logs against an extensive keyword list using high-performance **set comprehensions** ($O(1)$ lookups). This eliminates false positives (e.g., words like _DefaultSpeculator_ won't trigger a false _fault_ match).
- **Categorized Keyword Dictionary:** Built-in detection for a wide range of operational anomalies, including critical crashes, standard network/transaction failures, timeouts, and security warnings.
- **Error Counter & Statistics:** Keeps track of the total number of intercepted warnings/errors and provides a summary upon completing the export.
- **Interactive CLI Menu:** User-friendly terminal interface for fast navigation.

---

## 🛠️ How It Works

`Simple LogAnalyzer` processes your raw application logs through a clean, interactive flow:

```text
[Source Log File] ──> [Target Directory Input] ──> [Smart Header Parsing] ──> [Error Count & Custom Export File]
```
````

---

## 🚀 How to Use

Clone the repository and choose how you want to use it:

### 1. As an Interactive CLI Program

Simply run the main script and follow the on-screen instructions in your terminal to specify your file, output directory, and actions:

```bash
python main.py

```

### 2. As a Library in Your Own Python Code

Import the `LogAnalyzer` class directly into your backend scripts. The constructor now accepts both the input source and the target output path:

```python
from analyzer import LogAnalyzer

# Initialize the analyzer with your source log file and target output file path
analyzer = LogAnalyzer("my_app.log", "reports/errors_v1.txt")

# Display everything in the terminal
analyzer.showEverything()

# Extract, count, and save targeted errors/warnings directly to the specified output path
analyzer.filterWarnings()

```

---

🇵🇱

# Simple LogAnalyzer 📋🔍

Lekkie, modułowe narzędzie konsolowe stworzone do parsowania, filtrowania i wyodrębniania kluczowych błędów z nieuporządkowanych plików logów. Narzędzie może być używane bezpośrednio jako **interaktywne narzędzie CLI** lub zaimportowane jako **biblioteka obiektowa (OOP)** w innych projektach w Pythonie.

---

## 🌟 Główne Funkcje

- **Architektura OOP:** Czysta, obiektowa struktura z użyciem klas Pythona, ułatwiająca ponowne wykorzystanie kodu.
- **Zaawansowane zarządzanie ścieżkami:** Użytkownik wskazuje plik źródłowy oraz osobno definiuje dedykowany **folder zapisu** raportów za pomocą biblioteki `pathlib`.
- **Inteligentny algorytm parsowania:** Program analizuje pierwsze 4 wyrazy każdego wpisu, automatycznie oczyszcza je z interpunkcji i sprawdza dopasowania w oparciu o superwydajne wyrażenia zbiorotwórcze (**set comprehensions** – czas wyszukiwania $O(1)$). Zapobiega to fałszywym dopasowaniom (np. słowo _DefaultSpeculator_ nie wywoła już fałszywego alarmu dla słowa _fault_).
- **Szeroka baza słów kluczowych:** Wbudowana detekcja anomalii podzielona tematycznie (krytyczne awarie, błędy standardowe, problemy sieciowe/tranzakcyjne oraz ostrzeżenia bezpieczeństwa).
- **Licznik błędów i statystyki:** Program zlicza wszystkie dopasowane anomalie i wyświetla ich podsumowanie w konsoli po zakończeniu zapisu do pliku.
- **Interaktywne Menu CLI:** Przyjazny interfejs tekstowy umożliwiający szybką pracę z poziomu terminala.

---

## 🛠️ Jak To Działa

`Simple LogAnalyzer` przetwarza surowe logi aplikacji w prosty i interaktywny sposób:

```text
[Wskazany Plik Logu] ──> [Wybór Folderu Zapisu] ──> [Inteligentne Parsowanie] ──> [Podsumowanie i Plik Wyjściowy]

```

---

## 🚀 Jak Używać

Sklonuj repozytorium i wybierz preferowany sposób użycia:

### 1. Jako Interaktywny Program CLI

Uruchom główny skrypt i postępuj zgodnie z instrukcjami wyświetlanymi w terminalu, aby podać ścieżki oraz wywołać odpowiednie akcje:

```bash
python main.py

```

### 2. Jako Biblioteka w Twoim Własnym Kodzie

Zaimportuj klasę `LogAnalyzer` bezpośrednio do swoich skryptów backendowych. Konstruktor przyjmuje teraz zarówno plik wejściowy, jak i ścieżkę wyjściową:

```python
from analyzer import LogAnalyzer

# Zainicjalizuj analizator ze wskazanym plikiem źródłowym oraz docelowym plikiem raportu
analyzer = LogAnalyzer("logi_serwera.log", "raporty/wykryte_bledy.txt")

# Wyświetl wszystkie wpisy w konsoli
analyzer.showEverything()

# Przefiltruj, podsumuj i zapisz błędy bezpośrednio do zdefiniowanej wcześniej ścieżki docelowej
analyzer.filterWarnings()

```

```

---
```
