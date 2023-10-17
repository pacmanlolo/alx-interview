#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()

        # Parse the line using regular expressions to match the specified format
        import re
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            ip, status_code, file_size = match.groups()

            # Update metrics
            status_code = int(status_code)
            file_size = int(file_size)
            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

        if line_count % 10 == 0:
            print("Total file size: File size:", total_file_size)
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle CTRL+C interruption
    print("Total file size: File size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
