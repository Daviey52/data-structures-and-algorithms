from linked_list.linked_list import LinkedList

class Hashtable:
    pass
    def __init__(self, size=10024):
        self.size = size
        self.bucket = size *[None]

        # Initializer

    def hash(self, key):
        sum = 0
        for ch in key:
             sum += ord(ch)

        primed = sum * 97

        index = primed % self.size
        return index

    def add(self, key, value):
        index = self.hash(key)

        if not self.bucket[index]:
            self.bucket[index] = LinkedList()
        new_value = [key ,value]
        self.bucket[index].insert(new_value)


    def get(self, key):
        index = self.hash(key)
        if self.bucket[index]:
            LinkedList = self.bucket[index]
            currrent = LinkedList.head



    def contains():
        pass

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.


    def keys():
        pass

        # keys
        # Returns: Collection of keys

def repeated_word(sentence):
    word = sentence.split(" ")
    array1= []
    for ch in word:
        if ch in array1:

            return ch
        else:
            array1.append(ch.lower())



