

class Hashtable:
    pass
    def __init__(self, size=1024):
        self.size = size
        self.bucket = [None] * size

    def hash(self, key):
        sum = 0
        for ch in key:
             sum += ord(ch)
        primed = sum * 97
        index = primed % self.size
        return index

    def add(self, key, value):
        index = self.hash(key)
        if self.bucket[index] == None:
            self.bucket[index] = [[key,value],]
        self.bucket[index].append([key, value])

    def get(self, key):
        pass

    def contains(self,key):
        index = self.hash(key)
        if self.bucket[index]:
            return True
        else:
            return False

    def keys(self):
        for elements in self.bucket:
            return elements

def repeated_word(sentence):
    word = sentence.split(" ")
    array1= []
    for ch in word:
        if ch in array1:

            return ch
        else:
            array1.append(ch.lower())

if __name__ == "__main__":

    hashtable=Hashtable()
    hashtable.add('name','Dav')
    hashtable.add('age','27')
    hashtable.add('gold','Mal')
    hashtable.add('gold', 'dav')
    print(hashtable.hash('gold'))
    print(hashtable.contains('gold'))
    print(hashtable.contains('gold'))
    print(hashtable.keys())
    print(hashtable.get('gold'))
