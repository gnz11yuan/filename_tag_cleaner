#!/usr/bin/python
import os
import functools
import re
def split_line(text):
	words=functools.reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == "]" else acc + [elem], re.split("(])", text), [])
	return words

if __name__ == '__main__':
	path = input("Select path [current default]:")
	if not path:
		os.getcwd()
	else:
		os.chdir(path)
	while True:
		try:
			k=int(input("Tag position [starting with 0]:"))
			break
		except:
			print("Not a number")
	
	for name in os.listdir("."):
		if os.path.isdir(name):
			newList=split_line(name)
			newList.pop(k)
			newname="".join(newList)
			os.rename(name,newname)
			
