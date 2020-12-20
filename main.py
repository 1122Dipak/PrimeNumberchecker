def primeNumberchecker(num):
    number = int(num)
    if number > 1:
        for i in range(2,number//2):
            if number % i == 0:
                print("This is not a Prime Number.")
                break
            else:
                print("This is a Prime number.")
                break

    else:
        print("This is not a Prime number.")

primeNumberchecker(input("Check This Number :"))