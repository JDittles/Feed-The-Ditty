import requests

EdamamAppId = 'eceecbfb'
EdamamAppKey = '83347a87348057d5ab183aade8106646'

MealQuery = raw_input('What meal would you like to search for? ')

'''
The variable below can be used to add a string of parameters to our URL
by passing parameters to it in key-value pairs
'''
#MealPayload = {'key' : 'value1'}

EdamamSearchUrl = 'https://api.edamam.com/search?q=' + MealQuery + '&app_id=' + EdamamAppId + '&app_key=' + EdamamAppKey

#Putting Requests to work
r = requests.get(EdamamSearchUrl)
EdamamResponse = r.json()
#Thanks, Requests!

print(EdamamResponse)

'''
Learning the API's data structure is harder in Python.
EdamamResponse is the API's response with the JSON parsed.
The tag 'hits' gives us a list.
That list has a ton of attributes.
I'm tired and will check it out more later.
For now, I'm just leaving this guy printing the parsed JSON
'''

