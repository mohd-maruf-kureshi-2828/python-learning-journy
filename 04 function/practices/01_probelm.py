"""
def palindrome(str):
    rev_str=""
    for i in range(len(str)-1,-1,-1):
        rev_str+=str[i]
    if rev_str==str:
        print(f"Its A Palindrome {str}")
    else:
        print(f"Its Not A Palindrome {str}")

palindrome("mam")
palindrome("hello")
"""