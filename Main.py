import math
import LinkedList
import copy

m = 13 #number of rows in the hash table. Needs to be prime and not close to an exponent of 2
hash_table = {}
for i in range(0, m):
    hash_table[i] = LinkedList.linked_list()

def initialize():
    myfile = open("input.txt", "r")
    global docu
    docu = myfile.read()
    global word
    word = input("search: ")
    global l
    l = len(word)

# The point of prehashing (i.e. assigning numbers to items) is to achieve randomization -> we want to load each slot in
# the dict with approximately the same number of items in order to achieve a consistent and fast running time.
def prehash(data):
    output = math.floor(abs(hash(data)) % m)
    return output

def hashing(d):
    subsection = d[0:l]
    for i in range(0, len(d) - l + 1):
        hash_key = prehash(subsection)
        hash_table[hash_key].add_node(subsection)
        subsection = d[i + 1: l + i + 1]
    return hash_table

def print_hash_table(ht):
    copy1 = copy.deepcopy(ht)
    for i in copy1:
        string = ""
        cur_list = copy1[i]
        while cur_list.cur_node != None:
            string = string + str(cur_list.cur_node.data) + ", "
            cur_list.cur_node = cur_list.cur_node.next
        print(str(i) + "- Linked List: " + string)

def search_word(ht, w):
    total = ht[prehash(w)].count_node(w)
    return total

initialize()
hashing(docu)
#uncomment to visualize hash table:
#print_hash_table(hash_table)

print("Number of matches found: " + str(search_word(hash_table, word)))