#کلاس پشته را به 10 متد پیاده سازی کنید
class stack:
    def __init__(self ,z):
        self.items = [] * z
        self.z = z
        self.top = -1
    def push(self , item):
        if self.top >= self.z -1:
            print("stack is full")
            return
        self.items.append(item)
        self.top = self.top +1
    def pop(self):
        if self.top == -1:
            print("stack is empty")
            return
        return self.items.pop()
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top >= self.z-1
    def peek(self):
        if self.is_empty():
         return None
        return self.items[-1]
    def __len__(self):
        return len(self.items)    
    def __str__(self):
        return str(self.items)   
    def contatin(self,item):
        return item in self.items
    def chack(self):
        return self.top + 1 , self.z -(self.top + 1)
    def clear(self):
        self.items.clear()
    def show(self):
        print(self.items)
s = stack(10)
s.push(10)
s.push(20)
s.push(30)
x = s.pop()
print(s.chack())
print(s)
print(len(s))
print(s.peek())
print(s.is_empty())
print(x)
print(s.items)
print(s.contatin(50))
print(s.show())

