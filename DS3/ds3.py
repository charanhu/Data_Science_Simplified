# dict.get

locations = {'meeting1':'room1', 'meeting2':'room2'}

print(locations.get('meeting1', 'online'))

# to get the key that is not in the dict
print(locations.get('meeting3', 'online'))