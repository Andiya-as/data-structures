#متدی به کلاس پشته اضافه کنید که پنج لاگ اخر را نمایش دهد 
class stack:
    def __init__(self,z):
        self.list = [] *z
        self.top = -1
        self.z = z
    def push(self,x):
        if len(self.list) >= self.z:
            print("stack is full")
            return
        self.list.append(x)
        self.top +=1
    def is_empty(self):
        return self.top == -1
    def show_last_five_logs(self):
        if self.is_empty():
            print("stack is empty")
            return
        start = self.top -4

        if start <0:
            start = 0
        for i in range (start , self.top+1):
            print(self.list[i])
s = stack(15)
s.push("log 1")
s.push("log 2")
s.push("log 3")
s.push("log 4")
s.push("log 5")
s.push("log 6")
s.push("log 7")
s.show_last_five_logs()
