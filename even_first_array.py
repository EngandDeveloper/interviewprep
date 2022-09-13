''' 
*** Problem is from the book Elements Of Programming Interview With Python Chapter 5: Arrays
*** Problem Definition ***
Your input is an array of
integers, and you have to reorder its entries so that the even entries appear first. 
This is easy if you use O(n) space, where n is the length of the array. 
However, you are required to solve it without allocating additional storage.
'''

def reorder_array(arr):
  even_index = 0
  odd_index = len(arr) - 1
  while even_index < odd_index:
    if arr[even_index] % 2 == 0:
      even_index += 1
    else:
      arr[even_index], arr[odd_index] = arr[odd_idex], arr[even_index]
      odd_index -= 1
