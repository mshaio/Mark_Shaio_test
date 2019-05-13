Question3 missing functionalities:

1. After certain amount of time delete items in the cache that has expired. Applies to both region and global doubly
linked lists (not yet implemented)

2. When existing geolocation already exist the cache doesn't update correctly

3. Not yet automatically transition between closest region to retrieve data but regions have been set

4. Not fully implemeted the doubly linked list



General thoughts in solving Q3:
#1. Create a doubly linked list based on region (suppose our regions are Fredericton, Vancouver, Calgary and Montreal)
#2. Create a second doubly linked list containing every region
#3. Create a hash map to reference the linked list
#4. Create an algorithm that calculates the closest geolocation from source of request based on long and lat
# and returns the closest geolocation then use the doubly linked list for that geolocation. In the event that server
# is down use the global doubly linked list
#5. After certain amount of time delete items in the cache that has expired. Applies to both region and global doubly
# linked lists
