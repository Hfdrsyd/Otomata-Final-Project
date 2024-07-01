from collections import deque

def isPalindrome(string: str) -> bool:
    stack = deque()
    push = stack.append  # Alias for better readability
    pop = stack.pop
    
    length = len(string)
    mid = length // 2
    i = 0
    
    while i < mid:
        push(string[i])
        i += 1

    if length % 2 != 0:
        i += 1

    while i < length:
        if pop() != string[i]:
            return False
        i += 1
        
    return True
