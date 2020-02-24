#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    import copy
    import collections
    from collections import deque

    #with open(dictionary_file) as f:
       # xs = f.readlines()
    #print (xs)  --> shows us that each word ends with '\n'
    
    dictionary = open("words5.dict") #reads the file words5.dict
    listofwords = dictionary.read().split("\n")  #creates list of words
 

    s = []
    s.append(start_word)
    q = collections.deque()
    q.append(s)

    if start_word == end_word:
        return [end_word]

    while len(q) > 0:
        top = q.popleft()
        for word in set(listofwords):
           if _adjacent(word, top[-1]):
               if word == end_word:
                   top.append(word)
                   return top  
               stackcopy = copy.deepcopy(top) 
               stackcopy.append(word)
               q.append(stackcopy)
               listofwords.remove(word)
    return None
    
            
def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    counter = 0 
    for i in range(len(ladder)-1):
        if _adjacent(ladder[i], ladder[i+1]):
            counter += 1
        else:
            counter += 0
    if counter == len(ladder) - 1:
        return True
    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) == len(word2):
        counter = 0     # counter will check how many differences between word1 and word2
        for i in range(len(word1)):
            if word1[i] == word2[i]:  #if letter is same, counter will not update
                counter += 0 
            else:               #if letter is not same, counter will update
                counter += 1
        if counter == 1:    # if there is exactly one different letter
            return True
        else:
            return False    # if there is anything other than exactly 1 difference
    else:
        return False
