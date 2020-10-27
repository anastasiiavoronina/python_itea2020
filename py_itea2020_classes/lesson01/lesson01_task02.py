dict_countries = {
    'Ukraine': 'Kiev',
    'Poland' : 'Warsaw',
    'Great Britain' : 'London',
    'France' : 'Paris',
    'Belarus': 'Minsk'
}

list_countries = ['Spain', 'Poland', 'Ukraine', 'France', 'Italy', ' Norway', 'Greece']

for country in list_countries:
    if country in dict_countries:
        print(dict_countries[country] + ' is the capital of ' + country)
