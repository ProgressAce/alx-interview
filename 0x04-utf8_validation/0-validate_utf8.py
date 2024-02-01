#!/usr/bin/python3
"""Defines function to validate if data is of utf-8 encoding."""


def validUTF8(data):
    """Validates if data is of utf-8 capable, at the 1 byte level only."""

    if not isinstance(data, list):
        return False

    for int_char in data:
        if int_char < 0 or int_char > 255:
            return False

    return True
