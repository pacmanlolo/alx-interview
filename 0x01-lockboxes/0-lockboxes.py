#!/usr/bin/python3
def canUnlockAll(boxes):
    # Create a list to keep track of the opened boxes
    opened = [False] * len(boxes)
    opened[0] = True  # The first box is already open
    
    # Initialize a stack with the keys from the first box (box 0)
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box and that box is not opened yet
            if 0 <= key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)
    
    # If all boxes are opened, return True; otherwise, return False
    return all(opened)
