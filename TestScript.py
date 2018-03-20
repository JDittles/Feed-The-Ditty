import requests

EdamamAppId = 'eceecbfb'
EdamamAppKey = '83347a87348057d5ab183aade8106646'
EdamamQuery = 'chicken'
EdamamSearchUrl = 'https://api.edamam.com/search?q=' + EdamamQuery + 'chicken&app_id=$' + EdamamAppId + '&app_key=$' + EdamamAppKey + '&from=0&to=3&calories=591-722&health=alcohol-free'
r = requests.get(EdamamSearchUrl)
print(r.text)
