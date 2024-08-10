count = 0
while count < 5:
    try:
        num = int(input("Enter a Number: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("That's is not a valid number. please try again.")
    count += 1
print("End of loop.")