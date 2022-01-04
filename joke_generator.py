#!/usr/bin/python3
import random
import requests
import pprint
setup_list = []
punchline_list = []
for _ in range(3):
    r = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode')
    joke = r.json()
    #pprint.pprint(joke)
    setup = joke['setup']
    setup_list.append(setup)
    punchline = joke['delivery']
    punchline_list.append(punchline)

setup = setup_list[random.randrange(3)]
punchline = punchline_list[random.randrange(3)]

print("lawak hari ini\n")
print(setup)
print(punchline)

f = open('badjoke.txt','w')
f.write(setup)
f.write('\n')
f.write(punchline)
f.close()
