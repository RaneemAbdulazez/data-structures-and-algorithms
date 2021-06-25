from  .hashmap import Hashmap

def left_join_hash(ht_one,ht_two):
    hash_table = Hashmap()
    for elm in ht_one.map :
        if elm :
            hash_table.add(elm.head.data[0], [elm.head.data[1],None])
    for elm in ht_two.map :
        if elm :
            if hash_table.contains(elm.head.data[0]):
                hash_table.add(elm.head.data[0], [ht_one.get(elm.head.data[0]),elm.head.data[1]])

    return hash_table


if __name__ == "_main_":
    
  ht_one = Hashmap()
  ht_one.add('fond', 'enamored')
  ht_one.add('wrath', 'anger')
  ht_one.add('diligent', 'employed')
  ht_one.add('guide', 'garp')
  ht_one.add('outfit', 'usher')
  ht_two = Hashmap()
  ht_two.add('fond', 'averse')
  ht_two.add('wrath', 'delight')
  ht_two.add('diligent', 'idle')
  ht_two.add('guide', 'follow')
  ht_two.add('flow', 'jam')
  print(left_join_hash(ht_one, ht_two))