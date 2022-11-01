def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    x = len(s)
    a = x%2
    if a==1:
        return(s[x//2])
    b = x%2
    if b==0:
        return(s[x//2-1:x//2+1])

    
print(main('goccod'))