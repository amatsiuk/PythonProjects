def count_minimum_value (a,b,c,d,e):
    min=a
    if min > b:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if min > e:
        min = e
    print("min", min)

def count_maximum_value (a,b,c,d,e):
    max=a
    if max < b:
        max = b
    if max < c:
        max = c
    if max < d:
        max = d
    if max < e:
        max = e
    print("max", max)

count_minimum_value(3,6,1,8,4)
count_maximum_value(2,4,6,1,9)

