"""Code for implementation of a hash table. """

"""Uses separate chaining - hash table will have buckets array, with a linked list at each index of the buckets array.
This allows for collision resolution, when two keys have same hash value...
is alright because we can interate the list till we find the Node in the bucket."""


#50 buckets, i.e. capacity for internal array
INITIAL_CAPACITY = 50

#create Node data structure - essentially a LinkedList node, so has the self.next
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
    def __repr__(self):
        return str(self)


#hash table with functions
class HashTable:
    #initialize hash table
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        #current size, start at 0, can increase or decrease depending on insert or delete function
        self.size = 0
        #creates 50 none buckets
        self.buckets = [None]*self.capacity

