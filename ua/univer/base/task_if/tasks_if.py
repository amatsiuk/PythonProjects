def count_minimum_value(a, b, c, d, e):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if min > e:
        min = e
    print("min", min)


def count_maximum_value(a, b, c, d, e):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    print("max", max)


def check_name(name1, name2):
    if name1 == name2:
        print("The same Name")
    else:
        print("Not same Name")


def Season_of_the_year(x):
    if x == 1 or x == 2 or x == 12:
        print("Winter")
    if x == 3 or x == 4 or x == 5:
        print("Spring")
    if x == 6 or x == 7 or x == 8:
        print("Summer")
    if x == 9 or x == 10 or x == 11:
        print("Autum")
