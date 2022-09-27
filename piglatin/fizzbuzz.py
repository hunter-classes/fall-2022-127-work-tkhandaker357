def fizzbuzz():
    for number in range(1000):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        if number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

fizzbuzz()