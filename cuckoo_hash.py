import random
#random.seed(0)
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
        loc1 = self._hash1(key)
        loc2 = self._hash2(key)
        if self._array1[loc1]._key == key:
            return self._array1[loc1]._value
        elif self._array2[loc2]._key == key:
            return self._array2[loc2]._value
        else:
            raise "KeyError"

    def __setitem__(self,k,v): 
        ''' if key k exists in either array, modify associated value to v.
            if key k does not exist in both arrays, insert (k, v) into table as a new class Item.
            remember to modify size.
            if cycles, resize (rehash) the table.
            terminate the function until we finally find a location for k.
            You may want to use the _resize function for cycle 
        '''
        if k in self:
            loc1 = self._hash1(k)
            loc2 = self._hash2(k)
            if self._array1[loc1]._key == k:
                self._array1[loc1]._value = v
            else:
                self._array2[loc2]._value = v
        else:
            self._size += 1
            item = Item(k, v)
            loc1 = self._hash1(k)
            kick = self._array1[loc1]
            self._array1[loc1] = item
            count = 0
            while kick is not None and count <= 2 * len(self) - 1:                
                mid = kick
                loc2 = self._hash2(kick._key)
                kick = self._array2[loc2]
                self._array2[loc2] = mid
                count += 1
                if kick is None:
                    break
                loc1 = self._hash1(kick._key)
                mid = kick
                kick = self._array1[loc1]
                self._array1[loc1] = mid
                count += 1
            
            if count > 2 * len(self) - 1:
                for i in range(len(self._array1)):
                    if self._array1[i] is None:
                        self._array1[i] = kick
                        break
                    elif self._array2[i] is None:
                        self._array2[i] = kick
                        break
                self._resize()
   
                '''
                for i in range(self._maxsize):
                    if self._array1[i] is None:
                        self._array1[i] = kick
                        break
                    if self._array2[i] is None:
                        self._array2[i] = kick
                        break
                '''
            
        


    def __delitem__(self,k): 
        ''' given key, set self._array1 or self._array2 corresponding index to None.
            remember to modify size.
            raise KeyError if key not found.
        '''
        loc1 = self._hash1(k)
        loc2 = self._hash2(k)
        if self._array1[loc1] is None and self._array2[loc2] is None:
            raise KeyError
        if self._array1[loc1] is not None:
            if self._array1[loc1]._key == k:
                self._array1[loc1] = None
        if self._array2[loc2] is not None:
            if self._array2[loc2]._key == k:
                self._array2[loc2] = None
        
        self._size -= 1

    def _resize(self):
        ''' double the size of self._array1, self._array2.
            also self._maxsize
            Remember to rehash all the old (key, value) pairs!
        '''
        
        self._size = 0
        self._maxsize = 2 * self._maxsize
        mid1 = self._array1[:]
        mid2 = self._array2[:]
        self._array1 = [None] * self._maxsize
        self._array2 = [None] * self._maxsize
        for i in mid1:
            if i is not None:
                self[i._key] = i._value
        for i in mid2:
            if i is not None:
                self[i._key] = i._value
                
    def __len__(self): 
        return self._size

    def __contains__(self,key): 
        ''' return True if key exists in table
            return False otherwise
        ''' 
        loc1 = self._hash1(key)
        loc2 = self._hash2(key)
        if self._array1[loc1] is not None:
            return self._array1[loc1]._key == key
        elif self._array2[loc2] is not None:
            return self._array2[loc2]._key == key
        return False

    def __iter__(self):
        ''' same as keys(self) '''
        self.keys()

    def keys(self): 
        ''' yield an generator of keys in table '''
        for i in self._array1:
            if i is None:
                continue
            yield i._key
        for i in self._array2:
            if i is None:
                continue
            yield i._key

    def values(self): 
        ''' yield an generator of values in table '''
        for i in self._array1:
            if i is None:
                continue
            yield i._value
        for i in self._array2:
            if i is None:
                continue
            yield i._value

    def items(self):
        ''' yield an generator of Items in table '''
        for i in self._array1:
            if i is None:
                continue
            yield i
        for i in self._array2:
            if i is None:
                continue
            yield i


def main():
    table = CuckooHashTable()
    for i in range(200):        # Tests __setitem__, insert 0 ~ 199. _resize() also need to work correctly.
        table[i] = "happy_coding"
    
    print(len(table))           # Tests __len__, should be 200.

    for j in range(195):        # Tests __delitem__, delete 0 ~ 194
        del table[j]
        
    for j in table.items():     # Tests items()
        print(j._key)           # 195, 196, 197, 198, 199 left in table

    print(len(table))           # Tests __len__, should be 5.

    
    print(table[196])           # Tests __getitem__
##                                # Should print "happy_coding"
#    
if __name__ == '__main__':
    main()
