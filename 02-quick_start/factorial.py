# Python code​​​​​​‌‌‌‌​​‌‌​​‌‌‌‌​​‌‌​‌​​‌​‌ below

def factorial(num):
    if not isinstance(num, int):
        return
    if num < 0:
        return
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

print("factorial of 5 is", factorial(5))
print("factorial of 6 is", factorial(6))
print("factorial of 0.3 is", factorial(0.3))
print("factorial of -2 is", factorial(-2))
print("factor of spam spam spam is", factorial('spam spam spam'))
