import math


class LinkedList:
    def __init__(self):
        self.head = None
        self.order=0

    def addNode(self,coeff,exp):


        newNode = node(coeff,exp)
        if self.head == None:
            self.head = newNode
            newNode.next = newNode
            self.order = newNode.exp
            return

        current = self.head
        while True:
            if current.exp==exp:
                current.coeff = current.coeff + coeff
                # print("first")
                return
            current=current.next
            if current==self.head:
                # print("return")
                break

        # print("rest")

        last = self.head

        while (last.next != self.head):
            # print("rest")
            # secondlast=last
            last = last.next
        last.next = newNode
        newNode.next = self.head
        if newNode.exp>self.order:
            self.order=newNode.exp

        return

    def getPolynomial(self):
        current = self.head
        string = ""
        while True:
            string = string + str(math.trunc(current.coeff))+"t^"+str(math.trunc(current.exp))+" + "
            current=current.next
            if current == self.head:
                break
        string=string[:-3]
        return string
        del current

    def sum(self,poly1,poly2):
        current = poly1.head
        while True:
            self.addNode(current.coeff,current.exp)
            current=current.next
            if current == poly1.head:
                break

        current = poly2.head
        while True:
            self.addNode(current.coeff,current.exp)
            current=current.next
            if current == poly2.head:
                break

        print("sum:", self.getPolynomial())

    def sub(self,poly1,poly2):
        current = poly1.head
        while True:
            self.addNode(current.coeff,current.exp)
            current=current.next
            if current == poly1.head:
                break

        current = poly2.head
        while True:
            self.addNode(-current.coeff,current.exp)
            current=current.next
            if current == poly2.head:
                break

        print("sub:", self.getPolynomial())



    def evaluate(self,t):
        ans=0
        current = self.head
        while True:
            ans = ans + (current.coeff*pow(t,current.exp))
            current=current.next
            if current == self.head:
                break
        del current
        return ans
        # print("ans:",ans)


    def mult(self,poly1,poly2):

        current1 = poly1.head
        current2 = poly2.head
        while True:
            while True:
                coeff = current1.coeff * current2.coeff
                exp = current1.exp + current2.exp
                self.addNode(coeff,exp)
                current1=current1.next
                if current1 == poly1.head:
                    break
            current2=current2.next
            current1=poly1.head
            if current2==poly2.head:
                break
        print("mul:", self.getPolynomial())

        del current2
        del current1










class node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None



2x^2 +x^2


poly1=LinkedList()

poly1.addNode(2,2)
poly1.addNode(1,2)
poly1.addNode(3,1)
poly1.addNode(5,0)
print("poly1:",poly1.getPolynomial())

poly2=LinkedList()


poly2=LinkedList()

poly2.addNode(2 ,2)
poly2.addNode(4,1)
poly2.addNode(2,0)

print("poly2:",poly2.getPolynomial())


sum1=LinkedList()
sum1.sum(poly1,poly2)

# print("poly1:",poly1.getPolynomial())
# print("poly1:",poly1.getPolynomial())
# print("poly2:",poly2.getPolynomial())
sub1=LinkedList()
sub1.sub(poly1,poly2)



# print("poly1:",poly1.getPolynomial())




mul = LinkedList()
mul.mult(poly1,poly2)
print("poly1 at t=2:",poly1.evaluate(2))

# print("poly1:",poly1.getPolynomial())
# print("poly2:",poly2.getPolynomial())
# sum1.addNode(1,1)
# print("mul:",mul.getPolynomial())

