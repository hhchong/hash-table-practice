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

    #create the hash from a given key, if the key is a string
    #output will be a number from 0 to self.capacity (50 in this case)
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            #honestly there are different ways to do this, as long as it spreads it out among the internal bucket array
            hashsum += (idx + len(key)) ** ord(c)
            #modulo allows it to be in range 0 to self.capacity
            hashsum = hashum % self.capacity
        return hashsum

    #function to insert a key, value pair to the hashtable
    def insert(self, key, value):
        # increment the size of the hash table
        self.size += 1
        # get the new index aka hashed key
        index = self.hash(key)
        #go to the node corresponding to hash
        node = self.buckets[index]
        #if it is empty, create the node at the bucket and return
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        #if not empty, go to the end of the linked list at the bucket, create new node, but add it to the end
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    #function to find a data value based on a given key
    #input is the key, which is a string
    #output is the value stored under the key, or if there is no key, None
    def find(self, key):
        #get the hashed key
        index = self.hash(key)
        #go to the node in list at bucket
        node = self.buckets[index]
        #traverse the linked list at the node
        while node is not None and node.key != key:
            node = node.next
        # now node = the requested key value pair or it's None if it doesn't exist
        if node is None:
            return None

        else:
            return node.value

    #function to remove node stored at the given key
    #input is the key, which is a string
    #output is the value stored under the key, or if there is no key, None
    def remove(self, key):
        #get the hashed key and the node from the hashed key like past two functions
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        #iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        #now node is either the requested node or none
        if node is None:
            return None
        else:
            #node is found! let's delete it. decrement the size by 1
            self.size -= 1
            result = node.value
            if prev is None:
                #delete the node, node.next may be None or the next match
                self.buckets[index] = node.next
            else:
                #linkedlist delete, skips the next 
                prev.next = prev.next.next
            return result













