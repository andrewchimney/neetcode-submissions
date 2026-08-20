class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dyn_arr = [None] * capacity
        return

    def get(self, i: int) -> int:
        return self.dyn_arr[i]

    def set(self, i: int, n: int) -> None:
        self.dyn_arr[i]=n
        return

    def pushback(self, n: int) -> None:
        # if(n>self.capacity):
        #     self.resize()
        # for i in range(self.capacity):
        #     if self.dyn_arr[i] == n:
        #         self.dyn_arr[i] = None
        # self.dyn_arr[self.capacity-1]=n   
        if(self.getSize()==self.getCapacity()):
            self.resize()
        for i in range(self.capacity):
            if self.dyn_arr[i] is None:
                self.dyn_arr[i]=n
                return
        return

    def popback(self) -> int:
        last = self.dyn_arr[self.getSize()-1]
        self.dyn_arr[self.getSize()-1]=None
        return last
        

    def resize(self) -> None:
        for i in range(self.capacity):
            self.dyn_arr.append(None)
        self.capacity = self.capacity*2
        return

    def getSize(self) -> int:
        size=0
        for i in range(len(self.dyn_arr)):
            if self.dyn_arr[i] is not None: 
                size+=1
        return size
    
    def getCapacity(self) -> int:
        return self.capacity