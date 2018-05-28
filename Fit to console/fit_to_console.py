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
word=["hello1","hello2","hello3"]
length=len(word[0])+len(word[1])+len(word[2])
multi_factor = int( int(columns)/2 - (length/2) )
line = ("%s%s%s%s%s" % (word[0], "*"*multi_factor, word[1], "*"*multi_factor , word[2]))

print(line)
