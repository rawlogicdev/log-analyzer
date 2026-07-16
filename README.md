🇬🇧

# Simple LogAnalyzer 📋🔍

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/rawlogicdev/simple-loganalyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, modular, and terminal-based utility designed to parse, filter, and extract critical error logs from messy log files. This tool can be used either as an **interactive CLI tool** or imported as an **OOP library** in other Python projects.

---

## Key Features

- **OOP Architecture:** Clean object-oriented structure using Python classes, making it easily reusable.
- **Dynamic File Paths:** No hardcoded values. Input source and output export paths are defined by the user in real-time.
- **Bug Filtering:** Automatically detects warning, error, and critical patterns (`WARNING`, `ERROR`, `CRITICAL`) and isolates them.
- **Interactive CLI Menu:** User-friendly terminal interface for fast navigation.

---

## 🛠️ How It Works

`Simple LogAnalyzer` processes your raw application logs through a clean, interactive flow:

```text
[User Input Path] ──> [LogAnalyzer Object] ──> [Interactive CLI Menu] ──> [Custom export.txt]

```

---

## 🚀 How to Use

Clone the repository and choose how you want to use it:

### 1. As an Interactive CLI Program

Simply run the main script and follow the on-screen instructions in your terminal:

python main.py

### 2. As a Library in Your Own Python Code

Import the `LogAnalyzer` class directly into your backend scripts:

```python
from analyzer import LogAnalyzer

# Initialize the analyzer with your source log file
analyzer = LogAnalyzer("my_app.log")

# Display everything
analyzer.showEverything()

# Extract and save errors to a custom file
analyzer.filterWarnings("filtered_errors.txt")

```

---

🇵🇱

# Simple LogAnalyzer 📋🔍

Lekkie, modułowe narzędzie konsolowe stworzone do parsowania, filtrowania i wyodrębniania kluczowych błędów z nieuporządkowanych plików logów. Narzędzie może być używane bezpośrednio jako **interaktywne narzędzie CLI** lub zaimportowane jako **biblioteka obiektowa (OOP)** w innych projektach w Pythonie.

---

## Główne Funkcje

- **Architektura OOP:** Czysta, obiektowa struktura z użyciem klas Pythona, ułatwiająca ponowne wykorzystanie kodu.
- **Dynamiczne Ścieżki:** Brak sztywno wpisanych nazw plików. Ścieżka wejściowa i nazwa pliku wyjściowego są podawane przez użytkownika w czasie rzeczywistym.
- **Filtrowanie Błędów:** Automatycznie wykrywa błędy (`WARNING`, `ERROR`, `CRITICAL`) i izoluje je od reszty wpisów.
- **Interaktywne Menu CLI:** Przyjazny interfejs tekstowy umożliwiający szybką pracę z poziomu terminala.

---

## 🛠️ Jak To Działa

`Simple LogAnalyzer` przetwarza surowe logi aplikacji w prosty i interaktywny sposób:

```text
[Wskazany Plik Logu] ──> [Obiekt LogAnalyzer] ──> [Interaktywne Menu CLI] ──> [Własny plik wyjściowy]

```

---

## 🚀 Jak Używać

Sklonuj repozytorium i wybierz preferowany sposób użycia:

### 1. Jako Interaktywny Program CLI

Uruchom główny skrypt i postępuj zgodnie z instrukcjami wyświetlanymi w terminalu:

```bash
python main.py

```

### 2. Jako Biblioteka w Twoim Własnym Kodzie

Zaimportuj klasę `LogAnalyzer` bezpośrednio do swoich skryptów backendowych:

```python
from analyzer import LogAnalyzer

# Zainicjalizuj analizator ze wskazanym plikiem z logami
analyzer = LogAnalyzer("logi_serwera.log")

# Wyświetl wszystkie wpisy
analyzer.showEverything()

# Przefiltruj i zapisz błędy do nowego pliku
analyzer.filterWarnings("raport_bledow.txt")

```

```

---
```
