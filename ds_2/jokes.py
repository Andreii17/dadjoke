from dadjokes import Dadjoke, DadjokeSearch

dadjoke = Dadjoke()
print(dadjoke.joke)
print(type(dadjoke.joke))

my_term = 'coffe'
my_limit = 30
search = DadjokeSearch(term = my_term, limit = my_limit)
print(search)
print(type(search))
print(list(search))

for el in search:
    print(el.joke)