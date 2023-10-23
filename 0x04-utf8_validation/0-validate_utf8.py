#!/usr/bin/python3
def validUTF8(data):
    # Initialize a variable to keep track of the number of expected bytes for the next character.
    expected_bytes = 0
    
    # Iterate through each integer in the data list.
    for byte in data:
        # Check if the current byte is a continuation byte (starts with '10').
        if expected_bytes > 0:
            if (byte >> 6) == 0b10:
                expected_bytes -= 1
                return True
            else:
                return False
        else:
            # Determine the number of expected bytes for the current character.
            if (byte >> 7) == 0b0:
                expected_bytes = 0  # Single-byte character (0xxxxxxx)
            elif (byte >> 5) == 0b110:
                expected_bytes = 1  # Two-byte character (110xxxxx)
            elif (byte >> 4) == 0b1110:
                expected_bytes = 2  # Three-byte character (1110xxxx)
            elif (byte >> 3) == 0b11110:
                expected_bytes = 3  # Four-byte character (11110xxx)
            else:
                return False
