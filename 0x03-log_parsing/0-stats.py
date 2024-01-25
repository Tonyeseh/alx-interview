#!/usr/bin/python3
"""0-stats"""
import sys


def print_info(data, file_size):
    """prints stats of log"""
    keys = sorted(list(data.keys()))
    print("File size: {}".format(file_size))
    for key in keys:
        print("{}: {}".format(key, data.get(key, None)))


if __name__ == '__main__':
    data = {}
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            line_lst = line.split()

            if len(line_lst) < 5:
                continue

            try:
                count += 1
                code = int(line_lst[-2])
                size = int(line_lst[-1])

                if code in status_codes:
                    if code in data.keys():
                        data[code] += 1
                    else:
                        data[code] = 1
                    file_size += size

                if count == 10:
                    count = 0
                    print_info(data, file_size)

            except ValueError:
                continue

    except KeyboardInterrupt:
        print_info(data, file_size)
        raise
