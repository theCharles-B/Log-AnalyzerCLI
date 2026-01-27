# Log Inspector

Simple Python tool to analyze Linux log files and detect recurring error patterns.
Goal

### Help you quickly spot repeated failures in log files.
Features

- Read log files

- Count occurrences of error, warn, and fail

- Display a summary report in the CLI

### Usage

- JSON output

- Direct systemd log analysis via journalctl

- Automated tests with pytest

### Run the analyzer by passing the log file path:

bash
python log_inspector/analyzer.py /path/to/file.log

```bash
python log_inspector/analyzer.py /path/to/file.log
```
