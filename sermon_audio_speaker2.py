import urllib.parse
import urllib.request
import json
import time
from fake_useragent import UserAgent
import requests
import eyed3
import difflib
from difflib import get_close_matches

audiofile = eyed3.load("20210110-Sunday PM.mp3")
artist_info = audiofile.tag.artist 
album_info = audiofile.tag.album 
title_info = audiofile.tag.title 

print(artist_info + " " + album_info + " " + title_info)

#fake user agent so sermon audio doesn't block our api request
ua = UserAgent()

#url key and api key log in info to pull sermon info
url = 'https://api.sermonaudio.com/v1/node/speakers_for_source?sourceID=faithbaptistavon'
api_key = 'xxxxx-xxxxxxx-xxxxxxx'
#combines url log in info with a chrome user agent so we can later get the json payload to check if our steam is up 
hdr = {'X-Api-Key' : api_key,'User-Agent':str(ua.chrome)}
req = urllib.request.Request(url, headers=hdr)

with urllib.request.urlopen(req) as response:
    if response.getcode() == 200:
        source = response.read()
        the_page = json.loads(source)
        json_results = json.dumps(the_page)
        #empty list so we can populate with the speaker results
        name_results = []
        my_new_name_results = []
        #json response for number of speakers for so we can loop through the speakers 
        total_count_of_results = the_page['totalCount']
        #print(total_count_of_results)
        for speaker in range(total_count_of_results):
            #json for each indivudual speaker
            my_results = the_page['results'][speaker]['sortName']
            #print(the_page['results'][speaker]['sortName'])
            #puts each speaker into a list
            name_results.append(my_results)
        #This is where we split the last and first names in the list and then put them back together in a new list    
        for line in name_results:
            Type = line.split(",")
            lastName = Type[0]
            try : 
                firstName = Type[1]
            #Error handling for when there are a few entries that don't have a first name (If you put in Pastor as the first name it shows up blank and Uknown User)    
            except (IndexError) :
                firstName = str("")
            print(firstName, lastName)
            my_updated_names = firstName.lstrip(' ') + " " + lastName
            #new list/tuple with names swapped around
            my_new_name_results.append(my_updated_names)
        #print(my_new_name_results)
    else:
            print('An error occurred while attempting to retrieve data from the API.')

print(my_new_name_results)

close_match = difflib.get_close_matches(artist_info, my_new_name_results, n=3)
print(close_match)

if artist_info in close_match:
    print(artist_info)

# string not in the list
if artist_info not in close_match:
    print(close_match)
