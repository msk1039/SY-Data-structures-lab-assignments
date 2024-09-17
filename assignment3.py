import math


class LinkedList:
    def __init__(self):
        self.head = None
        self.order=0

    def addNode(self,coeff,exp):

        current = self.head
        while True:
            if current.exp==exp:
                current.coeff = current.coeff + coeff
                return
            current=current.next
            if current== self.head:
                return
        newNode = node(coeff,exp)
        if self.head == None:
            self.head = newNode
            newNode.next = newNode
            self.order = newNode.exp
            return

        last = self.head



        while (last.next != self.head):
            # secondlast=last
            last = last.next
        last.next = newNode
        newNode.next = self.head
        if newNode.exp>self.order:
            self.order=newNode.exp

        return

    def getPolynomial(self):
        current = self.head.next
        string = ""
        while current!=self.head:
            string = string + str(math.trunc(current.coeff))+"t^"+str(math.trunc(current.exp))+" + "
            current=current.next
        string=string[:-3]
        return string
        del current

    def sum(self,poly1,poly2):
        current = poly1.head.next
        while current!=poly1.head:
            self.addNode(current.coeff,current.exp)
            current=current.next

        current = poly2.head.next
        while current!=poly2.head:
            self.addNode(current.coeff,current.exp)
            current=current.next

        print("sum:", self.getPolynomial())

    def sub(self,poly1,poly2):
        current = poly1.head.next
        while current!=poly1.head:
            self.addNode(current.coeff,current.exp)
            current=current.next

        current = poly2.head.next
        while current!=poly2.head:
            self.addNode(-current.coeff,current.exp)
            current=current.next

        print("sub:", self.getPolynomial())



    def evaluate(self,t):
        ans=0
        current = self.head.next
        while current!=self.head:
            ans = ans + (current.coeff*pow(t,current.exp))
            current=current.next
        del current
        print("ans:",ans)


    def mult(self,poly1,poly2):

        current1 = poly1.head
        current2 = poly2.head
        while current2 is not None:
            while current1 is not None:
                coeff = current1.coeff * current2.coeff
                exp = current1.exp + current2.exp
                self.addNode(coeff,exp)
                current1=current1.next
            current2=current2.next
            current1=poly1.head
        print("mul:", self.getPolynomial())

        del current2
        del current1










class node:
    def __init__(self,coeff,exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None






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
# print("poly2:",poly2.getPolynomial())
sub1=LinkedList()
sub1.sub(poly1,poly2)



# print("poly1:",poly1.getPolynomial())




mul = LinkedList()
mul.mult(poly1,poly2)
poly1.evaluate(2)
# print("poly1:",poly1.getPolynomial())
# print("poly2:",poly2.getPolynomial())
# sum1.addNode(1,1)
# print("mul:",mul.getPolynomial())

