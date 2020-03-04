def power_a3():
    #a = int(input("enter number a: "))

    for i in range(5):
        b = i ** 3
        print(b)


def power_a234():
    # a = int(input("enter number a: "))
    # b = a ** 2
    # c = a ** 3
    # d = a ** 4
    for i in range(5):
        b = i ** 2
        c = i ** 3
        d = i ** 4
        print(b, c, d)


def menu():
    print("Enter 1 to chose procedure power_a3")
    print("Enter 2 to chose procedure power_a234")
    option = int(input("Make a choise"))
    if option == 1:
        result = power_a3()
    if option == 2:
        result = power_a234()
    print(result)







