def is_palindrome(number):
    str_n=str(number)
    if str_n == str_n[::-1]:
        return True
    else:
        return False
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
