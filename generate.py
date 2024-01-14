import requests, json, random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 1025)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''<p align="center">
    <img src="{result['sprites']['front_default']}" width="150" height="150">
</p>
<h3 align="center">You were embraced by - <b>{result['name'].title()}</b></h3>
<h3 align="center">Have a wonderful day!</h3>
''')
f.close()
