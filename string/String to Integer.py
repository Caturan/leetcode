def myAtoi(s: str) -> int:
    # Constants for 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Step 1: Remove leading whitespace
    s = s.lstrip()
    
    if not s:  # If string becomes empty after trimming whitespace
        return 0

    # Step 2: Handle sign
    sign = 1
    if s[0] in ('-', '+'):
        if s[0] == '-':
            sign = -1
        s = s[1:]  # Skip the sign character

    # Step 3: Read digits
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # Apply the sign
    result *= sign

    # Step 4: Clamp result to 32-bit integer range
    result = max(INT_MIN, min(INT_MAX, result))
    return result

s = "    -010 23 a b "
print(myAtoi(s))