import requests

EdamamAppId = 'eceecbfb'
EdamamAppKey = '83347a87348057d5ab183aade8106646'

MealQuery = raw_input('What meal would you like to search for? ')

EdamamSearchUrl = 'https://api.edamam.com/search?q=' + MealQuery + '&app_id=' + EdamamAppId + '&app_key=' + EdamamAppKey
r = requests.get(EdamamSearchUrl)
print(r.text)

