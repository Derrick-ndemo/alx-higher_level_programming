#!/usr/bin/python3

"""
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        tokens = line.strip().split()
        status_code = int(tokens[-2])
        file_size = int(tokens[-1])
        status_codes[status_code] += 1
        total_size += file_size

        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
except KeyboardInterrupt:
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
