# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets 
    that accepts string keys
    '''
    def __init__(self, capacity):
        #capacity attribute- Number of buckets in the hash table
        self.capacity = capacity
        #storage attribute- assinged to array set to noe * capacity
        self.storage = [None] * capacity
        
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # take the key and value
        # put it somewhere in the array
        # steps
        #get index for a key
        index = self._hash_mod(key)
        new_node = LinkedPair(key, value)
        if self.storage[index] is not None:
            print('ERR: Collision detected for key' + key)
            self.next = self.storage[index].value
            self.storage[index].value = self.next
        self.storage[index] = new_node
        

        #if collision place new linkedPair at the start of list



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #set a variable to the hash mode key
        index = self._hash_mod(key)
        #if no index in the storage
        if self.storage[index] is None:
            print('ERR: Nothing to delete')
        #else if there is a key
        elif self.storage[index].key == key:
            #set storage to none
            self.storage[index] = None
        #else
        else:
            #set current variable to index in storage
            current = self.storage[index]
            #set prev variable to none
            prev = None
            #while the current key is not equal to the key
            while current.key != key:
                #set prev to the current
                prev = current
                #set the curren to the next current index
                current = current.next
            #if the current key is equal to key
            if current.key == key:
                #set prev nex index to current next
                prev.next = current.next
                #set current to none
                current = None
            #if current is none
            elif current is None:
                #print non found
                print("Nothing found to be deleted")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # return associate value to key
        #if there is nothing in the key
        if self._hash_mod(key) is None:
            return None
        # get an index for the key
        index = self._hash_mod(key)
        return self.storage[index].value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2

        #create a new array size * 2
        self.storage = [None] * self.capacity

        #move all values over
        for pair in old_storage:
            #re-insert each key/value
            self.insert(pair.key, pair.value)


    

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
