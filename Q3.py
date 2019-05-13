"""
Question C

At Ormuco, we want to optimize every bits of software we write. Your goal is to
write a new library that can be integrated to the Ormuco stack. Dealing with
network issues everyday, latency is our biggest problem. Thus, your challenge is
to write a new Geo Distributed LRU (Least Recently Used) cache with time
expiration. This library will be used extensively by many of our services so it
needs to meet the following criteria:

1 - Simplicity. Integration needs to be dead simple.
2 - Resilient to network failures or crashes. #multiple linked lists + hashmaps representing the same thing?
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
4 - Data consistency across regions
5 - Locality of reference, data should almost always be available from the closest region
6 - Flexible Schema
7 - Cache can expire
"""

#Create a doubly linked list (next_node, prev_node and content (data + Geolocation, expiration time period))
#Create a hashmap

#1. Create a doubly linked list based on region (suppose our regions are Fredericton, Vancouver, Calgary and Montreal)
#2. Create a second doubly linked list containing every region
#3. Create a hash map to reference the linked list
#4. Create an algorithm that calculates the closest geolocation from source of request based on long and lat
# and returns the closest geolocation then use the doubly linked list for that geolocation. In the event that server
# is down use the global doubly linked list
#5. After certain amount of time delete items in the cache that has expired. Applies to both region and global doubly
# linked lists

from datetime import datetime
import math
# Node of a doubly linked list
class Node:
    def __init__(self, cache_length, next=None, prev=None, data=None):
        """Initialise a node in the cache

        Args:
            coche_length: Size of the cache
            next: Pointer to the next node (cache memory address)
            prev: Pointer to the previous node
            data: data in the cache, ie, content, geolocation and timestamp

        Returns:
            The return value. Returns void
        """
        self.next = next # reference to next node in DLL
        self.prev = prev # reference to previous node in DLL
        self.data = [] #Contatins content,geolocation and timestamp
        self.hash_map = {} #key is the data reference of the data and value is the index of where the data is at
        self.data_list = []
        self.cache_length = cache_length

    def insert_item(self, content_key,data_reference,data):
        """Insert requests in the hashmap and the linked list representing the
        cache. If the request is already in the hashmap do nothing to the
        hashmap and remove the request from the data list and put the request to
        the top of the data list. Otherwise add the request to the hashmap and
        put the item to the top of the data list. If the cache is full, ie the
        data list is full, remove the least recently used in the data list
        (which is the first item in a list) and add the new item to the list.
        Shift all requests down by one in the list. Lower index means older
        content.
        Args:
            content_key: Key of the hashmap
            data_reference: Value of the hashmap
            data: data in the cache, ie, content, geolocation and timestamp

        Returns:
            The return value. Returns void
        """
        self.data.append(data[0])#Content
        self.data.append(data[1])#Geolocation
        self.data.append(data[2])#timestamp

        if content_key not in self.hash_map:
            if len(self.hash_map) >= self.cache_length:
                content_key_to_remove = self.data_list[0][0] #LRU key
                self.remove_item(content_key_to_remove)#Removes the least recently used
        #Move the existing item to the head of item_list.
        #Remove item from cache list
        if content_key in self.hash_map:
            self.data_list.pop(self.hash_map.get(content_key))
            self.data_list.append(self.data)
        else:
            self.hash_map.update({content_key:data_reference})
            self.data_list.append(self.data)
        self.data = []
        print(self.hash_map)
        print(content_key, self.hash_map.get(content_key))
        return

    def remove_item(self,content_key):
        """Remove item from both the hashmap and the linked list

        Args:
            content_key: Key to the hashmap

        Returns:
            The return value. Returns void
        """
        self.data_list.pop(0)
        self.hash_map.pop(content_key)

        return

    def get_info(self):
        """Retrieves the content of cache

        Args:
            None

        Returns:
            The return value. Returns the content of cache as a list
        """
        return self.data_list

    def compute_region(self, long, lat):
        """Computes the distance between the location of request and the
        location of servers and return the closest server. Assume the distance
        can be calculated by taking the square root of the squares of long and
        lat. This does not take the arching of the earth into account but for
        production it must

        Args:
            long: longitude of the source of request.
            lat: latitude of the source of request.

        Returns:
            The return value. Returns the location (string) of the closest
            server with respect to the source of request.
        """
        long_lats = {vancouver : (0,0), calgary : (1,1), montreal : (2,2), fredericton : (3,3)}
        for i in long_lats:
          result = []
          x = long - long_lats.get(i)[0]
          y = lat - long_lats.get(i)[1]
          result.append(sqrt(x*x + y*y))
          closest = long_lats,index(min(result))
        return closest



if __name__ == "__main__":
    data1 = ["Geolocation from Fredericton", "Fredericton", datetime.now()]
    data2 = ["Geolocation from Montreal", "Montreal", datetime.now()]
    data3 = ["Geolocation from Vancouver", "Vancouver", datetime.now()]
    data4 = ["Geolocation from Calgary", "Calgary", datetime.now()]
    #data5 = ["Geolocation from Calgary", "Calgary", datetime.now()]
    region1 = Node(2)
    region2 = Node(2)
    region3 = Node(2)
    global_region = Node(2)
    #print(min(min(data1[2],data2[2]),data3[2]))
    #region1.add_cache_content(content1[0],content1[1],content1[2])
    region1.insert_item(data1[0],0,data1)
    region1.insert_item(data2[0],1,data2)
    region1.insert_item(data3[0],2,data3)
    region1.insert_item(data4[0],3,data4)
    #region1.insert_item(data5[0],4,data5)
    #region1.add_cache_content(content2[0],content2[1],content2[2])


print(region1.get_info())
