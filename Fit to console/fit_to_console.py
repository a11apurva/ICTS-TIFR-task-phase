import os
rows, columns = os.popen('stty size', 'r').read().split()

word="Hello!"

##Center
print("\n")
print(word.center(int(columns), '*'))
print("\n")
print(word.center(int(columns)))
print("\n")

##Right
print(('%'+str(int(columns)) +'s') %(word) )
print("\n")


##Left,Center,Right
