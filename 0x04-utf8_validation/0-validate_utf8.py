#!/usr/bin/python3
"""0-validate_utf8"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding"""
    chunk_no = 0
    # print([bin(chunk) for chunk in data])
    for chunk in data:
        chunk = bin(chunk)[2:][-8:]
        # print(chunk)
        # print("chunk number", chunk_no)
        if not chunk_no:
            if len(chunk) < 8:
                continue
            else:
                count = 1
                while chunk[count] == '1':
                    count += 1
                    chunk_no += 1

                if chunk_no > 3:
                    return False
        else:
            if chunk[:2] == '10':
                chunk_no -= 1
            else:
                return False

    if chunk_no > 0:
        return False

    return True
