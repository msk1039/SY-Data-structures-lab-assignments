class Linkedlist:
    def __init__(self):
        self.head=None

    def appendOrder(self, name, quantity,price):
        NewNode = order(name, quantity,price)
        NewNode.next = None
        if self.head is None:
            # NewNode.prev = None
            # self.head = NewNode
            self.head = NewNode
            NewNode.next = NewNode
            NewNode.prev = NewNode
            return
        last = self.head
        while (last.next is not self.head):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        NewNode.next = self.head
        self.head.prev = NewNode
        return

    def printOrders(self):
        current=self.head
        if current == None:
            print("list is empty")
            return

        while True:
            print("name:",current.name,"quantity:",current.quantity,"price:",current.price)
            current = current.next
            if current==self.head:
                break


    def searchItem(self,name):
        current=self.head
        while True:
            if name==current.name:
                print("item found")
                print("name:", current.name, "quantity:", current.quantity, "price:", current.price)
                return
            current = current.next
            if current==self.head:
                break
        print("item",name,"not found")
        return

    def deleteItem(self,name):
        current=self.head
        if current == None:
            print("list is empty")
        previous=current
        while True:
            if current.name == name:
                if current.prev == current or current.next == current:
                    self.head = None
                    del current
                    print("The Item:", name, " Deleted")
                    return
                if current==self.head:
                    self.head=current.next
                    self.head.prev=current.prev
                    current.prev.next=self.head
                    print("item", current.name, " deleted")
                    del current
                    return
                previous.next=current.next
                print("item", current.name, " deleted")
                del current
                return
            previous = current
            current = current.next
            if current==self.head:
                break
        print("item not found")
        return

    def update(self, name, newquantity, newprice):
        current = self.head
        if self.head == None:
            print("List is already empty.")
            return
        while True:
            if current.name == name:
                current.quantity = newquantity
                current.price = newprice
                print("The Item:", current.name, " has been updated")
                return
            current = current.next
            if current==self.head:
                print("item not found")
                return






class order:
    def __init__(self,name, quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.next = None
        self.prev = None


#
# orders = Linkedlist()
# orders.appendOrder("cola" , 2 , 20)
# orders.appendOrder("coffee" , 1 , 20)
# orders.appendOrder("vadapav" , 1 , 20)
# orders.searchItem("vadapav")
# orders.deleteItem("vadapav")
# orders.searchItem("vadapav")

#
# orders.printOrders()




def menu():
    orders = Linkedlist()
    while True:
        print("")
        print("MENU :-")
        print("1: Add item")
        print("2: Delete item")
        print("3: Search item")
        print("4: Update item")
        print("5: Display item")
        print("0: Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            inputname = input("Name: ")
            inputquantity = input("Quantity: ")
            inputprice = input("Price: ")
            orders.appendOrder(inputname , inputquantity , inputprice)
        elif choice == 2:
            inputname = input("Enter name of Item to be deleted: ")
            orders.deleteItem(inputname)
        elif choice == 3:
            inputname = input("Enter name of Item to search:")
            orders.searchItem(inputname)

        elif choice == 4:

            inputName = input("Enter name of item to be updated:")
            inputquantity = input("Enter updated quantity:")
            inputprice = input("Enter updated price:")
            orders.update(inputName, inputquantity, inputprice)
        elif choice == 5:
            orders.printOrders()
        elif choice == 0:
            return
        else:
            print("Enter a valid input")




menu()