class DynamicArray:
    #array vs dynamicArray- DA has the ability to resize
    def __init__(self, capacity=8):
        self.length = 0
        self.capacity = capacity
        #create a storage- make a list non is multiplited by 8, 
        # so it will create an array of that size
        # it will be a lot of NON in the array 
        self.storage = [None] * capacity

    #add functions
    def insert(self, index, value):
        #index helps to specify where we want
        # to add an index in

        #verify capacity if at capacity but there is a new number
        if self.length >= self.capacity:
            self.resize()
            # print("ERR: Array is full")
            # return
       
        # shit everything to the right of index, to the right
        for i in range(self.length, index, -1): 
            # consder that you will rune to the end of an element
            # going right to left to avoid an issue of checking empty space
            self.storage[i] = self.storage[i-1]
            #insert the value, at the index
            self.storage[index] = value
            self.length += 1
    def append(self, value):
        if self.length >= self.capacity:
            # print("ERR: Array is full")
            # return
            self.resize()
        self.storage[self.length] = value
        self.lenght += 1

        #if full we need to find a bigger block
        #of memory

    def resize(self):
        #create a new array, bigger in size
        self.capacity *= 2 #double the array size
        #create loop for all items in array to be moved
        for i in range(self.length):
        #create a new array
            new_storage = [None] * self.capacity
        #set the new array to storage
        self.storage = new_storage 


#DAY TWO OF HASH TABLES

# HASH FUNCTIONS- TURNS FUNCTIONS INTO A RANGE OF NUMBER
