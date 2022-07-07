def get_position(mystr: str) -> int:
    pos: int = 0
    
    for i in range(len(mystr)):
        if mystr[i] == '*':
            pos = i
            break
    
    return pos
