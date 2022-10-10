# python dictioanry get() method
# defination: The get() method returns the value of the item with the specified key if the key exists. 
# If the key does not exist, it returns the specified default value if specified, otherwise None.

locations = {'meeting1':'room1', 'meeting2':'room2'}

print(locations.get('meeting1', 'online'))
# Output: room1

# to get the default value if the key is not found
print(locations.get('meeting3', 'online'))
# Output: online