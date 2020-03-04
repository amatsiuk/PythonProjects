def do_smth(): pass


def task2( n=3, k=5):
    global i
        for i in range(n):
        print(k)


def task3(a,b):
    global i
    n = 0
    if a < b:
        for i in range(a, b + 1):
            print(i)
            n += 1
    else:
        print("not a<b")
    print("count=", n)


if __name__=="__main__":
    i=0
    while i<100:
        print(i)
        i+=1
        if i == 50:
            break

    for i in range(1,100):
        print(i)
        if i == 50:
            break


# Task 1
    for i in range(1,100):
        print(i, end="")


# Task 2
    task2()

# Task 3
    while True:
        begin = int(print("enter begin"))
        end = int(print("enter end"))
        task3(begin,end)
        answer = input("exit[y/n]")
        if answer == "y":
            break


# Task
    for i in range(10):
        for j in range(10):
            if (i==0 or i==9) or (j==0 or j==9):
                print("* ",end="")
            else:
                print("  ",end="")
        print()








