def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])

# print(count_recursively([1,2,3,3]))

def print_recursively(lst):
    """Print items in the list, using recursion."""

    #[1,2,3,4,5]

    if not lst:
        return
    print(lst[0])
    return(print_recursively(lst[1:]))

# print_recursively([1,2,3,4,5])

def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.
    Return None if needle is not in haystack.
    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    #recursive_index("hey", ["hey", "there", "you"])
    if not haystack:
        return None
    
    if haystack[0] == needle:
        return 0

    return 1 + recursive_index(needle, haystack[1:])

# print(recursive_index("hey", ["hello", "hi", "hiiii"]))
# THINK ABOUT THIS ONE MORE. ADDING AN INT TO NONETYPE ERRORS

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

    num_list = list(range(1,21))
    print(num_list)

    #loop through our list. If num is div by 3, print fizz. div by 5, print buzz. if num is div 5 and 3, print fizzbuzz.
    #we have to print fizzbuzz before the others bc if test for 3, and then 5 first, will never reach fizzbuzz.

    for num in num_list:
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

# fizzbuzz()

def translate_leet(phrase):
    """Translates input into "leet-speak"."""

    # put the letter and becomes as key value pairs
    # choosing a dictionary for fast look up when iterating over the string
    # create a dict
    # create new string to store new values
    # iterate over string
    # check if the c is in dict, if so, add value to the string
    # if c is not in dict, add existing c to string

    leet_dict = {
        "a" : "@",
        "o" : "0",
        "e" :  "3",
        "l" : "1",
        "s" : "5",
        "t" : "7"
    }

    new_phrase = ""
    for char in phrase:
        new_phrase += leet_dict.get(char.lower(), char)
    return new_phrase 

# print(translate_leet("Hackbright is the Shizzle"))

def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    current_word = ""
    new_list = []
    len_split=len(splitter)
    i=0
    while i < len(astring):
        if astring[i:i+len_split] == splitter:
            new_list.append(current_word)
            current_word = ""
            i += len_split
        else:
            current_word += astring[i]
            i += 1
    new_list.append(current_word)
    return new_list

# print(split("that is which is that which is that", " that "))

def rotate_grid(grid):
    """Given a square grid, rotate 180 degrees."""

    # Example grid: [ [1,2,3],
    #                 [4,5,6],
    #                 [7,8,9],
    #               ]

    # output grid: [ [9,8,7]
    #                [6,5,4]
    #                [3,2,1]  
    #               ]

    # method 1
    rev_grid = reversed(grid)
    new_grid = []
    for row in rev_grid:
        rev_row = reversed(row) #returns a "<list_reverseiterator object at 0x0043F190>"
        new_grid.append(rev_row)
    return new_grid

    # method 2
    rev_grid = reversed(grid)
    new_grid = []
    for row in rev_grid:
        rev_row = row[::-1] #returns the reversed list, not an iterator object
        new_grid.append(rev_row)
    return new_grid

# print(rotate_grid([ [1,2,3],[4,5,6],[7,8,9] ]))

