class Linkedlist:
    def __init__(self):
        self.head = None;

    def addAtEnd(self, name, disease, age):
        newNode = Patient(name, disease, age)
        if self.head == None:
            self.head = newNode
            return
        last = self.head
        while (last.next != None):
            last = last.next
        last.next = newNode
        print("patient",name,"added to the end")
        return

    def addAtBegin(self, name, disease, age):
        newNode = Patient(name, disease, age)
        newNode.next = self.head
        self.head = newNode
        print("patient",name,"added to the front")

    def listprint(self):
        printval = self.head
        while printval is not None:
            print("name:", printval.name, " disease:", printval.disease, " age:", printval.age)
            # print(printval,"nextadress:",printval.next)
            printval = printval.next


    def addAtMiddle(self, position, name, disease, age):
        newNode = Patient(name, disease, age)
        current = self.head
        for i in range(0, position - 1):
            behind = current
            current = current.next

        newNode.next = current
        behind.next = newNode
        print("patient",name,"added at position:",position)

    def delete(self,position):
        current = self.head

        if position==1:
            self.head = current.next
            del current
            return

        for i in range(0, position - 1):
            behind = current
            current = current.next
            

        behind.next=current.next
        print("patient",current.name,"have been discharged")
        del current

    def search(self , name):
        current = self.head
        position=0
        while(current!=None):
            position += 1
            if name==current.name:
                # print("patient found at position",position)
                return position
            current=current.next
        print("patient not found")

        return 1


    def sendToFront(self,name):
        position = self.search(name)
        current = self.head

        for i in range(0, position - 1):
            behind = current
            current = current.next
        behind.next=current.next
        current.next=self.head
        self.head=current
        print("patient,",name,"sent to the front for emergancy")

    def updateData(self,name):

        position = self.search(name)
        print("enter updated name disease and age")
        updateList = []

        for i in range(0,3):
            ele = input()
            updateList.append(ele)

        current = self.head
        for i in range(0, position - 1):
            current = current.next

        current.updatePatient(updateList[0],updateList[1],updateList[2])

    def displayPatient(self,name):
        current = self.head
        position = 0
        while (current != None):
            position += 1
            if name == current.name:
                print("patient found at position",position)
                print("name:",current.name)
                print("disease:",current.disease)
                print("age:", current.age)
            current = current.next
        print("patient not found")

class Patient:
    def __init__(self, name, disease, age):
        self.name = name
        self.disease = disease
        self.age = age
        self.next = None

    def updatePatient(self , newName , newDisease , newAge):
        self.name = newName
        self.disease = newDisease
        self.age = newAge
    

def menu():

    queue = Linkedlist()


    while True:
        print("enter choice")
        print("1:add patient")
        print("2:discharge patient")
        print("3:update patient")
        print("4:Display all patients")
        print("5:search patient")
        print("6:send patient to the front")
        print("0:exit")
        choice = int(input())
        if choice==1:
            print("where to add patient?")
            print("1:add at front")
            print("2:add at middle")
            print("3:add at end")
            addChoice=int(input())
            if addChoice==1:
                print("enter name , disease and age of the patient:     ")
                inputName=input()
                inputDisease = input()
                inputAge = input()
                queue.addAtBegin(inputName, inputDisease, inputAge)
            elif addChoice==2:
                print("enter name , disease and age of the patient: ")
                inputName=input()
                inputDisease = input()
                inputAge = input()
                pos = int(input("enter the position: "))
                queue.addAtMiddle(pos,inputName, inputDisease, inputAge)
            elif addChoice==3:
                print("enter name , disease and age of the patient: ")
                inputName = input()
                inputDisease = input()
                inputAge = input()
                queue.addAtEnd( inputName, inputDisease, inputAge)
            else:
                print("invalid input")

        elif choice==2:
            dischargePatient=input("enter name of patient to be discharged: ")
            dischargePosition=queue.search(dischargePatient)
            queue.delete(dischargePosition)

        elif choice==3:
            updatePatientName=input("enter tha name of patient to be updated: ")
            queue.updateData(updatePatientName)
        elif choice==4:
            queue.listprint()

        elif choice==5:
            searchPatientName=input("enter name of patient to be searched: ")
            queue.displayPatient(searchPatientName)

        elif choice==6:
            sendPatientToFront = input("enter the name of the patient to send to front: ")
            queue.sendToFront(sendPatientToFront)
        elif choice==0:
            return
        else:
            print("invalid input")




menu()
# queue = Queue()
#
# queue.addAtEnd("jay", "cold", 18)
# queue.addAtEnd("mayank", "sardi", 18)
# queue.addAtBegin("anuj", "fever", 18)
# queue.addAtMiddle(3, "varad ", "pile", 18)
# queue.addAtBegin("pratik", "fever", 18)
# queue.addAtBegin("rohit", "fever", 18)
# queue.addAtBegin("avishkar", "fever", 18)
# queue.addAtBegin("amit", "fever", 18)
# queue.delete(4)
# queue.search("anuj")
# queue.sendToFront(5)
# queue.updateData("avishkar")
# queue.listprint()