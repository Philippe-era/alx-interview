#!/usr/bin/python3
"""list will be unlocked by this script"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    pairs = [0]
    for pair in pairs:
        for num in boxes[pair]:
            if num not in pairs and num < len(boxes):
                pairs.append(num)
    if len(pairs) == len(boxes):
        return True
    return False
