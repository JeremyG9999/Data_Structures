import os
import time
from scripts.linked_list import main as LinkedList
from scripts.doubly_link_list import main as DoublyLinkedList
from scripts.stack import main as Stack
from scripts.queue_list import main as Queue
from scripts.binary_tree import main as Binary_Tree

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a choice:")
            print("1. Run Singly Linked List")
            print("2. Run Doubly Linked List")
            print("3. Run Stack")
            print("4. Run Queue")
            print("5. Run Binary Tree")
            print("6. Clear Terminal")
            print("7. Exit")
            option = input("Select a menu option: ")
            if option == "1":
                self.cls()
                LinkedList()
            elif option == "2":
                self.cls()
                DoublyLinkedList()
            elif option == "3":
                self.cls()
                Stack()
            elif option == "4":
                self.cls()
                Queue()
            elif option == "5":
                self.cls()
                Binary_Tree()
            elif option == "6":
                self.cls()
            elif option == "7":
                break
            else:
                print("Invalid input")

    def cls(self):
        time.sleep(0.2)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    Menu().main_menu()