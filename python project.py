fibonaci=[0, 1, 1, 2, 3, 5, 8, 13,21,34,55,89,144,233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28567, 46368, 75025, 121393, 196418, 317811]
def process(*number):
    numbers=list(number)
    for i in range(len(number)):
        if number[i] in fibonaci:
            print(f"---{numbers[i]} is a fibonaci number.---")
        else:
            print(f"---{numbers[i]} is not valid fibonaci number.---")




while True:
    choice=input("Do you want to START/KILL Press(S/K): ")
    if  choice == 's':
        

        process(int(input("Enter any Desired Number: ")),int(input("Enter any Desired Number: ")))
    else:
        exit()