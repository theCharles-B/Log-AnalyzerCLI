from collections import Counter
import re
import argparse
from pathlib import Path

PATTERNS = re.compile(r"(error|fail|warn)", re.IGNORECASE)

def analyze_log(file_path) -> Counter:
    counter = Counter()

    with file_path.open('r', errors='ignore') as f:
        for line in f:
            match = PATTERNS.search(line)
            if match:
                counter[match.group(1).lower()] += 1
    return counter

def main():
    parser = argparse.ArgumentParser(
        description="Analyze log files for error, fail, and warn patterns."
    )
    parser.add_argument(
        "log_files",
        type=Path,
        help="Path to the log file(s) to analyze.",
    )

    args = parser.parse_args()

    if not args.log_files.exists():
        print(f"File {args.log_files} does not exist.")
        return
    
    result = analyze_log(args.log_files)

    print("Analysis Results:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
