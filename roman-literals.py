#
# Description is here: https://leetcode.com/problems/roman-to-integer/
#
result=0
class Solution:
    def romanToInt(self, s: str) -> int:
        global result
        result=0
        return(first_digit(0,s))

def first_digit(sp:int, s: str):
    global result
    if (sp == len(s)):
        return (result)
    print (s[sp])
    if (s[sp] == 'M'):
        result = result+1000
        return (first_digit(sp+1,s))
    elif (s[sp] == 'D'):
        result = result+500
        return (first_digit(sp+1,s))
    elif (s[sp] == 'C'):
        return(handle_C(sp+1,s))
    elif (s[sp] == 'L'):
        result = result+50
        return (first_digit(sp+1,s))
    elif (s[sp] == 'V'):
        result = result+5
        return (first_digit(sp+1,s))
    elif (s[sp] == 'X'):
        return (handle_X(sp+1,s))
    elif (s[sp] == 'I'):
        return (handle_I(sp+1,s))
        

def handle_C(sp:int, s: str):
    global result
    if (sp == len(s)):
        result = result+100
        print (result)
        return (result)
    elif (s[sp] == 'C'):
        result = result + 100
        print(result)
        return (handle_C(sp+1,s))
    elif (s[sp] == 'D'):
        result = result+400
        return (first_digit(sp+1,s))
    elif (s[sp] == 'M'):
        result = result+900
        return (first_digit(sp+1,s))
    else:
        result = result+100
        return (first_digit(sp,s))
    print (s[sp])

def handle_X(sp:int, s: str):
    global result
    if (sp == len(s)):
        result = result+10
        print (result)
        return (result)
    elif (s[sp] == 'X'):
        result = result + 10
        print(result)
        return (handle_X(sp+1,s))
    elif (s[sp] == 'L'):
        result = result+40
        return (first_digit(sp+1,s))
    elif (s[sp] == 'C'):
        result = result+90
        return (first_digit(sp+1,s))
    else:
        result = result+10
        return (first_digit(sp,s))
    print (s[sp])

def handle_I(sp:int, s: str):
    global result
    if (sp == len(s)):
        result = result+1
        print (result)
        return (result)
    elif (s[sp] == 'I'):
        result = result + 1
        print(result)
        return (handle_I(sp+1,s))
    elif (s[sp] == 'V'):
        result = result+4
        return (first_digit(sp+1,s))
    elif (s[sp] == 'X'):
        result = result+9
        return (first_digit(sp+1,s))
    else:
        result = result+1
        return (first_digit(sp,s))
    print (s[sp])
