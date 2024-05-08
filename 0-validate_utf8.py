#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Checks if a given data set
    displays a valid utf-8 encoding
    """
    number_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for initial in data:

        mask_byte = 1 << 7

        if number_b == 0:

            while mask_byte & i:
                number_b += 1
                mask_byte = mask_byte >> 1

            if number_b == 0:
                continue

            if number_b == 1 or number_b > 4:
                return False

        else:
            if not (initial & mask_1 and not (initial & mask_2)):
                return False

        number_b -= 1

    if number_b == 0:
        return True

    return False
