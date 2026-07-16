class LogAnalyzer:
    def __init__(self, file_source):
        self.source = file_source

    def showEverything(self):
        try:
            with open(self.source, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"ERROR: Couldnt find the file {self.source}")

    def filterWarnings(self, warningFile):
        try:
            with open(self.source, "r", encoding="utf-8") as infile, \
                 open(warningFile, "w", encoding="utf-8") as outfile:
                
                for line in infile:
                    if "ERROR" in line or "WARNING" in line or "CRITICAL" in line:
                        print(line.strip())
                        outfile.write(line) 

            
            print(f"\n[INFO] Filtered warnings available in {warningFile}")
           
        except FileNotFoundError:
            print(f"ERROR: Source file {self.source} does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")