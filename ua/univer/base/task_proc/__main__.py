from ua.univer.base.task_proc import proc_menu
from ua.univer.base.task_proc.proc_menu import power_a3, power_a234, menu


def main():
    choice = "y"
    while choice == "y":
        menu()
        choice = input("try again[y/n]")

if __name__=="__main__":
    main()

