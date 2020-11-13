import shelve

FILE = 'COUNTRIES'

def add_country_and_capital(country, capital):

    with shelve.open(FILE) as db:
        db[country] = capital

def get_capital_by_country(country):
    with shelve.open(FILE) as db:
        return db.get(country, 'No such country in th DB')

#add_country_and_capital('Ukraine', 'Kyiv')
#add_country_and_capital('Belarus', 'Minsk')

print(get_capital_by_country('Ukraine'))