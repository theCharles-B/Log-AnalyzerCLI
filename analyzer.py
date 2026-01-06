from collections import Counter
import re
import sys

PATTERNS = re.compile(r"(error|fail|warn)", re.IGNORECASE)

def analyze_log(file_path):
    counter = Counter()

    with open(file_path, 'r', errors='ignore') as f:
        for line in f:
            match = PATTERNS.search(line)
            if match:
                counter[match.group(1).lower()] += 1

    return counter

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    result = analyze_log(log_file_path)
   
    print("Log Analysis Results:")
    for key, value in result.items():
        print(f"{key}: {value}")
