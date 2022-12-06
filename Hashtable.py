class HashTable():
    def __init__(self, lenght: int)-> None:
        self.max_lenght = lenght
        self.data = [None for i in range(lenght)]
    

    def __get_hash_by_key(self, key) -> int:
        return hash(key)
    
    def __get_index_by_hash(self, _hash: int) -> int:
        return _hash % self.max_lenght
    
    def get_index(self, key) -> int:
        hash_ = self.__get_hash_by_key(key)
        index_ = self.__get_index_by_hash(hash_)
        return index_
    
    def __getitem__(self, key):
        hash_ = self.__get_hash_by_key(key)
        index_ = self.__get_index_by_hash(hash_)
        return self.data[index_]


    def set(self, key, value):
        index_ = self.get_index(key)
        self.data[index_] = value
        return value

    def get(self, key):
        index_ = self.get_index(key)
        return self.data[index_]

    def update(self, key, value):
        index_ = self.get_index(key)
        self.data[index_] = value
        return value
        

h = HashTable(10)

h.set("ybsdt", 15)
h.set("yasdfasdft", 15)
h.set("ysdfasdfasdft", 15)
h.set("asdfasfasfwuiot", 15)
h.set("ybakyttelt", 15)
h.set("ykkjjejjeert", 15)
h.set("yytt", 15)
print(h[1])
print(h.data)

