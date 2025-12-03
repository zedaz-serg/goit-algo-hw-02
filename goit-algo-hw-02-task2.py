from collections import deque
import re

def is_palindrome_deque(input_string: str) -> bool:
    
    cleaned_string = re.sub(r'[^a-z0-9]', '', input_string.lower())
    
    if len(cleaned_string) < 2:
        return True

    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        
        first_char = char_deque.popleft()
        last_char = char_deque.pop()
        
        if first_char != last_char:
            return False
            
    return True