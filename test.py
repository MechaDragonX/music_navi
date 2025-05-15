from spotapi import Public

url_prefix = 'https://open.spotify.com/track/'

results = Public.song_search('sunny yorushika')
track_info = ''
for item in results:
    # For some reason I need to do index with a number to get the first sub result even though it errors... this API is stupid
    track_info = item[0].__str__()
    break

# - get index where uri starting with 'spotify:track:' begins
# - generate substring from that index to end
# - split it at ' to isolate URI from the rest
# - get the 0th element so I just have the URI
# - return substring following 'spotify:track:'
id = track_info[track_info.find('spotify:track:'):].split('\'')[0][14:]
url = f'{url_prefix}{id}'
print(url)
