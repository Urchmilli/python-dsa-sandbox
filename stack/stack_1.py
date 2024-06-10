# Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from stack import Stack 

def reverse_string(str):
    s = Stack()
    for i in str:
        s.push(i)

    rev_str = ""
    while s.size() > 0:
        rev_str += s.pop()
    
    return rev_str

string_1 = "We will overcome covid19"
print(reverse_string(string_1))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def is_match(ch1, ch2):
    match_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch==']':
            if stack.size()==0:
                return False
            if not is_match(ch, stack.pop()):
                return False
    return stack.size()==0 

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))