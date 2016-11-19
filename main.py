#!/usr/bin/python3

import sys
from imports import prefRandOut

input = ""

for arg in sys.argv[1:]:
	input = input + " " +arg

input = input.lower()

def greet():
	print("Hey! This is YoBro")

greetings = ['hi','hello','hey','heya']

for greets in greetings:
	if input.find(greets):
		greet()
		break
