#!/usr/bin/python

import sys
import urllib2
import json

def get_term(term):
  url = 'http://api.urbandictionary.com/v0/define?term='+term
  return url

def get_random():
  url = 'http://api.urbandictionary.com/v0/random'
  return url


def main():
  args = sys.argv[1:]
  
  if not args:
    url = get_random()
  else:
    url = get_term(args[0])
  
  response = urllib2.urlopen(url).read()
  data = json.loads(response)
  for item in range(len(data['list'])):
    print data['list'][item]['definition']
    print data['list'][item]['permalink']
    print '\n'

if __name__ == '__main__':
  main()
