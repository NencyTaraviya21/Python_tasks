#'_' it's inbuilt variable which stores the value of the preceding printed value.

#string,list---

s = 'First line.\nSecond line.'  # \n means newline
s       # without print(), special characters are included in the string
print(s)  # with print(), special characters are interpreted, so \n produces new line


print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#prefix = 'Py'
#prefix 'thon'  (# can't concatenate a variable and a string literal)

#word='examination'
#word[42]  (# the word only has 11 characters)

word='examination'
word[4:42] #but slicing allows this 

#list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']

#control flow tools...

#for--

words = ['hello', 'hi', 'bye']
for w in words:
    print(w, len(w))

#pass Statements -->  It can be used when a program is required syntactically but the program requires no action
class MyEmptyClass:
    pass

#match Statements--> works as switch statements

def http_error(status):
    match status:
        case 401 | 403 | 404:       #(can combine several literals in a single pattern)
            return "Not allowed"


#'__match_args__'--> define a specific position for attributes in patterns by setting the '__match_args__' special attribute in your classes

class xyz:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match xyz:
    case []:
        print("No points")
    case [xyz(0, 0)]:
        print("The origin")
    case [xyz(x, y)]:
        print(f"Single point {x}, {y}")


