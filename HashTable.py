# Hash Map
class HashTable:
    def __init__(self):
        self.Max=100
        self.arr=[None for i in range(self.Max)]

    def get_hash(self, key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.Max
    
    def add_item(self,key,value):
        h=self.get_hash(key)
        self.arr[h]=value

    def get_item(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    
    def del_item(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

    def print_arr(self):
        print(self.arr)
Table1=HashTable()
Table1.add_item('y',1)
Table1.add_item('u',2)
Table1.add_item('g',3)
print(Table1.get_item('g'))
print(Table1.print_arr())
Table1.del_item('y')
print(Table1.print_arr())