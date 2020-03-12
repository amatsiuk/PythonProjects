def main():
    arr = [1,2,3,4,5,6,7,8,9]
    arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    with open("int_arr.txt","a") as file:
        count = 0
        for i in arr1:
            file.write(str(i))
            count += 1
            if count <= len(arr1):
                file.write(";")
        file.write("\n\r")
    arr_read = []
    with open("int_arr.txt","r") as read_file:
        for row in read_file:
            print(row)
            list_str = row.split(";")
            for word in list_str:
                arr_read.append(int(word))
            print(arr_read)



def matrix_example():
    users = [
        ["Tom", 32, "+380975556677"],
        ["Bob", 32, "+380976663355"],
        ["Alice", 19, "+380977772233"]
    ]
    for user in users:
        if (user[1] > 20):
            print(user)


def sort_example():
    arr = [2, 5, 3, 6, 67, 34, 89, 21, 5, 89]
    print(arr)
    sort_arr = sorted(arr)
    print(sort_arr)
    print(arr)


if __name__ == '__main__':
    main()
