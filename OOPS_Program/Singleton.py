def singleton(func):
    lst = []
    def inner():
        if len(lst) == 0:
            lst.append(func())
        return lst[0]
    return inner

@singleton
class Ticket:
    def __init__(self):
        self.seats = 250
    
    def book(self, num):
        self.seats -= num
        print(self.seats)

c1 = Ticket()
c2 = Ticket()

c1.book(50)
c2.book(50)