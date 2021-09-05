print("Palindrome".center(75, "="))
palindrome = input("Input Kata : ")
b = ""
for a in palindrome:
    b = a + b
if (palindrome == b):
    print("Benar Kata Palindrome")
else:
    print("Salah! Bukan Kata Palindrome")
