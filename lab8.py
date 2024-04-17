import re
from typing import List, Dict
from dataclasses import dataclass

@dataclass(frozen=True)
class LogEntry:
    timestamp: str
    message: str

def read_log_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_log_entry(line: str) -> LogEntry:
    match = re.match(r'\[(.*?)\]\s(.*)', line)
    if match:
        timestamp, message = match.groups()
        return LogEntry(timestamp=timestamp, message=message.strip())
    else:
        return None

def process_logs(log_lines: List[str]) -> List[LogEntry]:
    return list(filter(None, map(parse_log_entry, log_lines)))

def analyze_logs(log_entries: List[LogEntry]) -> Dict[str, int]:
    return {level: sum(1 for entry in log_entries if entry.message.startswith(level)) for level in set(entry.message.split()[0] for entry in log_entries)}

def main():
    log_file_path = 'example.log'
    log_lines = read_log_file(log_file_path)
    log_entries = process_logs(log_lines)
    log_analysis = analyze_logs(log_entries)
    for level, count in log_analysis.items():
        print(f"{level} логтау деңгейінде : {count} жазба")

if __name__ == "__main__":
    main()
