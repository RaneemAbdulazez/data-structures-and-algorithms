from datastructures.linked_list.linked_list import *
class Hashmap:
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size

    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hashed_key = (sum *19)% self.size
        return hashed_key

    def __str__(self):
        output = []

        for i in self.map:
            if i:
                current = i.head
                while current:
                    output.append(' -> '.join(current.value))
                    current = current.next
        string_hash = ' ,'.join(output)
        return string_hash


    def add(self, key, value):
       hashed_key = self.hash(key)
       if self.contains(key):
            current = self.map[hashed_key].head
            while current:
                if key == current.value[0]:
                    current.value[1] =  value
                current = current.next
                return self
       if not self.map[hashed_key]:
           self.map[hashed_key] = LinkedList()
       self.map[hashed_key].append([ key, value])
       return self.__str__()




    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if key == current.value[0] :
                    return current.value[1]
                current = current.next
        return "not found"



    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            current = self.map[index].head
            while current:
                if key == current.value[0]:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    hash_map = Hashmap()
    print(hash_map.add('python','Machine learnign '))
    hash_map.add('python','web development')
    hash_map.add('javascript','web development')
    hash_map.add('java','mobile application')
    hash_map.add('C#','game development')
    print(hash_map.get('python'))
    print(hash_map)
    print('pass')
