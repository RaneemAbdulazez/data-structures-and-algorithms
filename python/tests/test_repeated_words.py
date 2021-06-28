from challenges.repeated_word.repeated_word import Hash_map

hashmp=Hash_map()


def test_empty():
    input_str="Once upon a time, there was a brave princess who..."
    actual=hashmp.first_repeated(input_str)
    excepted='a'
    assert excepted==actual
    
    
def test_valid_input1():
    input_str='It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    actual=hashmp.first_repeated(input_str)
    excepted='was'
    assert excepted==actual
    
    
def test_valid_input_2():
    input_str='It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    actual=hashmp.first_repeated(input_str)
    excepted='It'
    assert excepted==actual

