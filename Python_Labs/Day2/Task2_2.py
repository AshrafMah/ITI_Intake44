'''
write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is divisible by both return "FizzBuzz"
'''


def divisible(number):
    if number % 3 == 0 and number % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return number


num = int(input("Enter a number: "))
isDivisible = divisible(num)
print(isDivisible)
