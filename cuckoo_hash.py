import random

class Item():
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __eq__(self, other):               
        return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
        return not (self == other)       # opposite of __eq__

    def __lt__(self, other):               
        return self._key < other._key    # compare items based on their keys

class CuckooHashTable():
    def __init__(self):
        self._size=0
        self._maxsize = 11
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        self._random1 = random.random()
        self._random2 = random.random()


    def _hash1(self, key):
        return hash((key, self._random1)) % self._maxsize

    def _hash2(self, key):
        return hash((key, self._random2)) % self._maxsize


    def __getitem__(self,key):
        ''' given key, return the value associated with key
            use hash1/hash2 to compute the index.
            raise KeyError if not found.
        '''
        pass

    def __setitem__(self,k,v): 
        ''' if key k exists in either array, modify associated value to v.
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item.
            remember to modify size.
            if cycles, resize (rehash) the table.
            terminate the function until we finally find a location for k.
            You may want to use the _resize function for cycle 
        '''
        pass
        


    def __delitem__(self,k): 
        ''' given key, set self._array1 or self._array2 corresponding index to None.
            remember to modify size.
            raise KeyError if key not found.
        '''
        pass

    def _resize(self):
        ''' double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        '''
        pass

    def __len__(self): 
        pass

    def __contains__(self,key): 
        ''' return True if key exists in table
            return False otherwise
        '''
        pass

    def __iter__(self):
        ''' same as keys(self) '''
        pass

    def keys(self): 
        ''' yield an generator of keys in table '''
        pass

    def values(self): 
        ''' yield an generator of values in table '''
        pass

    def items(self):
        ''' yield an generator of Items in table '''
        pass


def main():
    table = CuckooHashTable()
    for i in range(200):        # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
        table[i] = "happy_coding"
    
    print(len(table))           # Tests __len__, should be 200.

    for j in range(195):        # Tests __delitem__, delete 0 ~ 194
        del table[j]

    print(len(table))           # Tests __len__, should be 5.

    for j in table.items():     # Tests items()
        print(j._key)           # 195, 196, 197, 198, 199 left in table

    print(table[196])           # Tests __getitem__
                                # Should print "happy_coding"
    
if __name__ == '__main__':
    main()
