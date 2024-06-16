#Bubble sort, it is a popular sorting algorithm
#-> The time complexity is O(n**2) -> Quadratic 
#-> Space complexity is O(1) -> Constant time


def bubble_sort(element, key=None):
    size = len(element)
    
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                swapped = True

        if not swapped:
            break 
              
if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements, key="name")
    #bubble_sort(elements, key="transaction_amount")
   
    print(elements)
    
