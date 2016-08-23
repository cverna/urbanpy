#!/usr/bin/python
from argparse import ArgumentParser
import requests


parser = ArgumentParser(description="Uses urbandictionary api to get a term definition")
parser.add_argument('term', type=str, nargs='*', help='term to be define')
args = parser.parse_args()

if args.term:
    req = requests.get('http://api.urbandictionary.com/v0/define?term='+args.term[0])
    req = req.json()
    nb_answer = 3
else:
    req = requests.get('http://api.urbandictionary.com/v0/random')
    req = req.json()
    nb_answer = 1


if len(req['list']) < nb_answer:
    nb_answer = len(req['list'])

for item in range(nb_answer):
    print
    print req['list'][item]['definition']
    print req['list'][item]['permalink']
    print '------------------------------------------------------------------------'
    print
