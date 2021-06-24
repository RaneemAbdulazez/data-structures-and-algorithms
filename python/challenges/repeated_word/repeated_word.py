import re
class Hash_map():
    def __init__(self,size=1024):
        self.size=size
        self.buckets=[None]*size
        
        
        
    def hashing_function(self,key):
        sum=0
        for i in key :
            sum=(sum+ord(i)*key.index(i)*19)%self.size
        return sum
    
    
    def add(self,key):
        index=self.hashing_function(key)
        if not self.buckets[index]:
            self.buckets[index]=key
            return None
        return key
    
    def first_repeated(self,input_string):
        if input_string=="":
            return 'not valid'
        input_string=re.sub(r'[^\w\s]','',input_string)
        split_string=input_string.split(" ")
        for word in split_string:
            if self.add(word):
                return word

        return 'no words repearted'        
        
        
                        
            
if __name__=="__main__":
    hshp=Hash_map()
    hshp.add('ehllo')
        
    