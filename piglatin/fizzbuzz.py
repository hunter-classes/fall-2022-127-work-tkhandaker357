def fizzbuzz(n):
    for number in range(int(n) + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

print("Input a number to fizzbuzz: ")
number = input()
fizzbuzz(number)