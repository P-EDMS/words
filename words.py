#!/usr/bin/python -tt
# Copyright 2015 Panton.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. Implment a funciton to scan

2. Implement a function to filter:
  - [String->List] clean up the whitespaces and unnecessarily punctuation marks.
  - [List-> ]

3. Implement a function to index

"""

import sys
import re
import os.path
import timeit


def scan(filename):
  input_file = open(filename, 'rU')
  word_list = []



  for line in input_file:
    filter(line.lower(), word_list)

  print sorted(word_list), len(word_list)

def filter(line, word_list):


  words = re.findall(r'[^\s\W]+[\'\w]+', line)
  for word in words:
    if word not in word_list:
      word_list.append(word)

def main():

  if len(sys.argv) < 2:
    print 'usage: ./indexing.py file'
    sys.exit(1)
	

  filename = sys.argv[1]

  if not os.path.isfile(filename):
    print 'error: please ensure that the file exists'
    sys.exit(1)

  scan(filename)


if __name__ == '__main__':
  main()


