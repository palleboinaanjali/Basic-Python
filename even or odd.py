def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

try:
    num = int(input("Enter a number: "))
    check_even_odd(num)
except ValueError:
    print("Please enter a valid integer.")

