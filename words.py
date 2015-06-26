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
import time


def scan(filename):
  input_file = open(filename, 'rU')
  
  #dict is choosen over list, O(1) for read.
  word_list = {}
  start = time.time()
  #by EOF, we should be able to received a bunch of words
  for line in input_file:
    filter(line.lower(), word_list)
  end = time.time()

  input_file.close()

  print sorted(word_list), len(word_list)
  print "scan&filter: %f" % (end - start)



""" 

1. remove whitespaces & punctuation marks.
2. look from database
	2.1 reserved words
	2.2 existing words

  
"""

def filter(line, word_list):
  words = re.findall(r'[^\s\W]+[\'\w]+', line)
  for word in words:
    if word not in word_list:
      word_list.update({word: 0})

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
  start = time.time()
  main()
  end = time.time()
  print "whole program: %f" % (end - start)




