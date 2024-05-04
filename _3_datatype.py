# Python Data Types are used to define the type of a variable. It defines what type of data we are going to store in a variable.

# Text Type:	str  =>  "hell world"
# Numeric Types:	int, float, complex  =>  3, 20.5, 2j
# Sequence Types:	list, tuple, range   =>  ["apple", "banana", "cherry"] / ("apple", "banana", "cherry") / range(6)
# Mapping Type:	dict  => {"name" : "John", "age" : 36}
# Set Types:	set, frozenset  =>  {"apple", "banana", "cherry"}  // frozenset({"apple", "banana", "cherry"})
# Boolean Type:	bool  =>  True
# Binary Types:	bytes, bytearray, memoryview  =>  b"Hello" // bytearray(5) //  memoryview(bytes(5))
# None Type:	NoneType  =>  None

#-----------------------------------------------------------------------------------------------------
#     SUBSTRING
#-----------------------------------------------------------------------------------------------------
# str = 'Hello World!'
# print (str)          # Prints complete string // 'Hello World!'
# print (str[0])       # Prints first character of the string // H
# print (str[2:5])     # Prints characters starting from 3rd to 5th  //  llo
# print (str[2:])      # Prints string starting from 3rd character till the end // llo World!
# print (str * 2)      # Prints string two times  // Hello World!Hello World!
# print (str + "TEST") # Prints concatenated string // Hello World!TEST


#-----------------------------------------------------------------------------------------------------
#     LIST
#-----------------------------------------------------------------------------------------------------
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
#
# print (list)            # Prints complete list // ['abcd', 786, 2.23, 'john', 70.2]
# print (list[0])         # Prints first element of the list // abcd
# print (list[1:3])       # Prints elements starting from 2nd till 3rd// [786, 2.23]
# print (list[2:])        # Prints elements starting from 3rd element // [2.23, 'john', 70.2]
# print (tinylist * 2)    # Prints list two times /// [123, 'john', 123, 'john']
# print (list + tinylist) # Prints concatenated lists// ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']


#-----------------------------------------------------------------------------------------------------
#     Tuple
#-----------------------------------------------------------------------------------------------------
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')
#
# print (tuple)               # Prints the complete tuple  //  ('abcd', 786, 2.23, 'john', 70.2)
# print (tuple[0])            # Prints first element of the tuple  //  abcd
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd  //  (786, 2.23)
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element  //  (2.23, 'john', 70.2)
# print (tinytuple * 2)       # Prints the contents of the tuple twice  //  (123, 'john', 123, 'john')
# print (tuple + tinytuple)   # Prints concatenated tuples  //  ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
#
# # NOTE THAT TUPLES ARE IMMUTABLE. CA NOT BE CHANGED
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
# list[2] = 1000     # Valid syntax with list

#-----------------------------------------------------------------------------------------------------
#     RANGE  - Python range() is an in-built function in Python which returns a sequence of numbers starting from 0 and increments to 1 until it reaches a specified number.
#-----------------------------------------------------------------------------------------------------
# range(start, stop, step)
    # start: Integer number to specify starting position, (Its optional, Default: 0)
    # stop: Integer number to specify starting position (It's mandatory)
    # step: Integer number to specify increment, (Its optional, Default: 1)
 # therefore:
    # range(10) is [0,1,2,3,4,5,6,7,8,9] #here you supplied only stop i.e range(stop)
    # range(0,10) is [0,1,2,3,4,5,6,7,8,9] # here you specified where to start and where to stop
    # range(2,10) is [2,3,4,5,6,7,8,9] # here you specified to start at 3rd index and where to stop
    # range(2,10,2) is [2,4,6,8] # here you specified to start at 3rd index and stop at the 10th index but move 2 steps
        # ths, assuming [0,1,2,3,4,5,6,7,8,9] is the 10 items from 0 index, you ask it to start from 3 index by ssupplying 2 as start, you get [2,3,4,5,6,7,8,9],
        # now you said from [2,3,4,5,6,7,8,9], it should move 2 steps, then the final output will skip the ordd mumbers and you get [2,4,6,8]

# EXAMPLE -- range(stop)
#for i in range(5):
  # print(i)

# OUTPUT
# 0
# 1
# 2
# 3
# 4

# # EXAMPLE  -- range(start,stop)
# for i in range(1, 5):
#   print(i)

# OUTPUT
# 1
# 2
# 3
# 4


# # EXAMPLE  -- range(start,stop,step)
# for i in range(1, 5, 2):
#   print(i)
#
# # OUTPUT
# 1
# 3




#-----------------------------------------------------------------------------------------------------
#     DICIONARY
#-----------------------------------------------------------------------------------------------------
# Python dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.
# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
#
# print (dict['one'])       # Prints value for 'one' key  //This is one
# print (dict[2])           # Prints value for 2 key  //This is two
# print (tinydict)          # Prints complete dictionary  //{'dept': 'sales', 'code': 6734, 'name': 'john'}
# print (tinydict.keys())   # Prints all the keys  //['dept', 'code', 'name']
# print (tinydict.values()) # Prints all the values  //  ['sales', 6734, 'john']







#
# print (tuple)               # Prints the complete tuple  //  ('abcd', 786, 2.23, 'john', 70.2)
# print (tuple[0])            # Prints first element of the tuple  //  abcd
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd  //  (786, 2.23)
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element  //  (2.23, 'john', 70.2)
# print (tinytuple * 2)       # Prints the contents of the tuple twice  //  (123, 'john', 123, 'john')
# print (tuple + tinytuple)   # Prints concatenated tuples  //  ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
#
# # NOTE THAT TUPLES ARE IMMUTABLE. CA NOT BE CHANGED
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
# list[2] = 1000     # Valid syntax with list


#-----------------------------------------------------------------------------------------------------
#     LIST
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#     LIST
#-----------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------
#     COVERTING/CASTING
#-----------------------------------------------------------------------------------------------------
#
# int(x [,base])  //  Converts x to an integer. base specifies the base if x is a string.
# long(x [,base] ) //Converts x to a long integer. base specifies the base if x is a string.
# float(x) // Converts x to a floating-point number.
# complex(real [,imag]) //Creates a complex number.
# str(x) // Converts object x to a string representation.
# repr(x) //Converts object x to an expression string.
# eval(str) // Evaluates a string and returns an object.
# tuple(s) //  Converts s to a tuple.
# list(s) // Converts s to a list.
# set(s) // Converts s to a set.
# dict(d) // Creates a dictionary. d must be a sequence of (key,value) tuples.
# frozenset(s) / Converts s to a frozen set.
# chr(x) // Converts an integer to a character.
#  unichr(x) //Converts an integer to a Unicode character.
# ord(x) // Converts a single character to its integer value.
# hex(x) // Converts an integer to a hexadecimal string.
# oct(x)  // Converts an integer to an octal string.
