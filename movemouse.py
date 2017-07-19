#!/usr/bin/python

import sys
import time
from random import randint
from pynput.mouse import Controller

mouse = Controller()
i = 60
t = 60

try:
	i = int(sys.argv[1])
	t = int(sys.argv[2])
except:
	pass 

print('Running ' + str(i) + ' iterations of ' + str(t) + ' seconds...')

# Set pointer position

for i in range(0, i):
	x = randint(600, 700)
	y = randint(400, 500)
	mouse.position = (x, y)
	print('Moved mouse pointer to {0}'.format(
    	mouse.position) + ' sleeping '+ str(t) +' seconds')
	time.sleep(t)
