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
        try:
            with open(self.source, "r", encoding="utf-8") as infile, \
                 open(self.output, "w", encoding="utf-8") as outfile:
                
                for line in infile:
                    line_lower = line.lower()
                    
                    if any(keyword in line_lower for keyword in self.KEYWORDS):
                        print(line.strip())
                        outfile.write(line) 

            print(f"\n[INFO] Filtered warnings available in {self.output}")
           
        except FileNotFoundError:
            print(f"ERROR: Source file {self.source} does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
