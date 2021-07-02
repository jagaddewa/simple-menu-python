import sys
import os


    
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear') #'nt' means Windows OS

def main_menu():
    clear_screen()
    print("Welcome to sample program")
    print("Please choose the menu you want to choose:")
    print("1. Menu 1")
    print("2. Menu 2")
    print("0. Exit")
    
def sub_menu():
    clear_screen()
    print("Welcome to sub-menu:")
    print("1. Sub-menu 1")
    print("0. Back to main menu")
    
def back_to_menu():
    print()
    input("Press enter to back")
    
    
    
def menus():
    loop1=True
    while loop1:
        main_menu()
        choices=int(input("Enter the choice [0-2]: "))
        
        if choices==1:
            clear_screen()
            print("This is menu 1's content")
            back_to_menu()
        elif choices==2:
            clear_screen()
            loop2=True
            while loop2:
                sub_menu()
                choices2=int(input("Enter the choice [0-1]: "))
                if choices2==1:
                    clear_screen()
                    print("This is sub-menu 1's content")
                    back_to_menu()
                elif choices2==0:
                    clear_screen()
                    print("Thanks for visiting sub-menu")
                    loop2=False
                    back_to_menu()
        elif choices==0:
            print("You are exiting program, thank you for attention")
            loop1=False
            sys.exit(1)
            break
           
           
if __name__=='__main__':
    menus()