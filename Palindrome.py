def isPalindrome(string: str) -> bool:
    return string == string[::-1]

string = input("Enter word: ")

if isPalindrome(string):
    print(f"{string} adalah Palindrome")
else:
    print(f"{string} bukan Palindrome")
