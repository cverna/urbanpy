#!/usr/bin/python

import sys
import urllib2
import json
import argparse

def getTerm (term):
  
  url = 'http://api.urbandictionary.com/v0/define?term='+term
  return url

def getRandom ():
  url = 'http://api.urbandictionary.com/v0/random'
  return url


def main ():
  
  args = sys.argv[1:]
  
  if not args:
    url = getRandom()
  else :
    url = getTerm(args[0])
  
  response = urllib2.urlopen(url).read()
  data = json.loads(response)
  for item in range(len(data['list'])):
    print data['list'][item]['definition']
    print data['list'][item]['permalink']
    print '\n'

if __name__ == '__main__':
  main()
