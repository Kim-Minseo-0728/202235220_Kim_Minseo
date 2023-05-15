import random
arr = []
for value in range(0,20):
    arr.append(random.randint(0, 100))
print (arr)
print(type(arr))




#Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Node_Mgmt:
    def __init__(self, head):
        self.head = head  

    #Binary_Put
    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:  
                    self.current_node = self.current_node.left  
                else:
                    self.current_node.left = Node(value)  
                    break
            else:
                if self.current_node.right != None:  
                    self.current_node = self.current_node.right  
                else:
                    self.current_node.right = Node(value)
                    break

    #Binary_Search
    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:  
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left  
            else:
                self.current_node = self.current_node.right  
        return False  

    #Binary_Delete
    def delete(self, value):
        self.current_node = self.head  
        self.parent = self.head  

        
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.curent_node = self.current_node.left  
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right  

        if searched == False:  
            return False

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.current_node.left != None and self.current_node.right == None:
            
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        if self.current_node.left != None and self.current_node.right != None:

            
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                self.change_node = self.change_node.left

                
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:  
                    self.change_node_parent.left = None

               
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
        else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.chage_node = self.change_node.left  
                
                if self.chage_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:  
                    self.change_node_parent.left = None

                
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.chage_node.right = self.current_node.right

#Selection
def selection_sort(a):
    for i in range(len(a) - 1):
        md = i
    for j in range(i + 1, len(a)):
        if a[j] < a[md]:
            md = j
    a[i], a[md] = a[md], a[i]

#Bubble
def bubble_sort(b):
    for i in range(len(b) - 1, 0, -1):
        for j in range(i):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]

#Insertion
def insertion_sort(c):
    for i in range(len(c)):
        for j in range(i, 0, -1):
            if c[j - 1] > c[j]:
                c[j - 1], c[j] = c[j], c[j - 1]

#Merge
def merge_sort(d):
    if len(d) < 2:
        return d

    mid = len(d) // 2
    low_arr = merge_sort(d[:mid])
    high_arr = merge_sort(d[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

#Quick
def quick_sort(e):
    if len(e) <= 1:
        return e
    pivot = e[len(e) // 2]
    l_arr, e_arr, g_arr = [], [], []
    for num in e:
        if num < pivot:
            l_arr.append(num)
        elif num > pivot:
            g_arr.append(num)
        else:
            e_arr.append(num)
    return quick_sort(l_arr) + e_arr + quick_sort(g_arr)

#Heap_Put
def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

#Heap_Sort
def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)

  return unsorted



