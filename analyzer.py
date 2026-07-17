class LogAnalyzer:
    KEYWORDS = [
        # --- KRYTYCZNE AWARIE (System przestaje działać) ---
        "critical", "crit", "fatal", "emergency", "emerg", "panic", "alert", "crash", 
        "deadlock", "corrupted", "unrecoverable", "bluescreen", "bsod", "kernel_panic",
        
        # --- STANDARDOWE BŁĘDY (Operacja się nie udała) ---
        "error", "err", "failed", "failure", "fail", "exception", "severe", "rejected", 
        "refused", "denied", "forbidden", "unauthorized", "invalid", "abort", "aborted",
        "missing", "dropped", "terminated", "killed", "fault", "interrupted",
        
        # --- PROBLEMY SIECIOWE I TRANZAKCYJNE ---
        "timeout", "timedout", "disconnected", "unreachable", "retry_exhausted", 
        "overloaded", "unavailable", "bad_gateway", "connection_lost",
        
        # --- OSTRZEŻENIA (Potencjalne problemy / Bezpieczeństwo) ---
        "warning", "warn", "wrn", "attention", "deprecated", "deprecation", "obsolete",
        "slow_query", "leak", "high_memory", "high_cpu", "low_disk", "suspicious"
    ]

    def __init__(self, file_source, output_target):
        self.source = file_source 
        self.output = output_target

    def showEverything(self):
        try:
            with open(self.source, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"ERROR: Couldnt find the file {self.source}")

    def filterWarnings(self):
        keywords_set = {kw.lower() for kw in self.KEYWORDS}
        found_errors_count = 0
        try:
            with open(self.source, "r", encoding="utf-8") as infile, \
                 open(self.output, "w", encoding="utf-8") as outfile:
                
                for line in infile:
                    words = line.split() # zmiana calej lini na osobne wyrazy (robi sie lista)
                    if not words:
                        continue
                    
                    beggining_words = [w.strip("[],.:;()\"'").lower() for w in words[:4]] # bierzemy tylko 4 pierwsze wyrazy z listy, stripujemy je z interpunkcji i filtrujemy je
                    beggining_text = " ".join(beggining_words).lower() # zmieniamy liste spowrotem w stringa 
                    
                    if any(word in keywords_set for word in beggining_words):
                        outfile.write(line) 
                        found_errors_count += 1

            print(f"\n[INFO] Filtered warnings available in {self.output}")
            print(f"\n[INFO] Total errors found: {found_errors_count}")
            
           
        except FileNotFoundError:
            print(f"ERROR: Source file {self.source} does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
