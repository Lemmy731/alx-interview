#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        # Extract the file size and status code
        size = int(parts[-1])
        code = parts[-2]
        
        # Update the total size and status code count
        total_size += size
        if code in status_codes:
            status_codes[code] += 1

        line_count += 1
        
        # Print every 10 lines
        if line_count % 10 == 0:
            print_stats()
            
except KeyboardInterrupt:
    # On a keyboard interrupt, print the stats
    print_stats()
    raise

# Print the final stats after the loop ends
print_stats()
