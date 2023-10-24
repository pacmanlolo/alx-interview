#!/usr/bin/python3
def validUTF8(data):
    # Initialize a variable to keep track of the number of bytes remaining for the current character
    bytes_remaining = 0

    # Iterate through each integer in the list
    for byte in data:
        # Check if the most significant bit is 0, indicating it's a start of a new character
        if bytes_remaining == 0:
            if (byte >> 7) == 0b0:
                bytes_remaining = 0
            elif (byte >> 5) == 0b110:
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:
                bytes_remaining = 3
            else:
                return False
        else:
            # If it's not a start of a new character, it should start with the bit pattern '10'
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # If all bytes have been used, it's valid UTF-8
    return bytes_remaining == 0
