import os
rows, columns = os.popen('stty size', 'r').read().split()
print(' MENU '.center(int(columns), '*'))
print(' MENU '.center(int(columns)))
