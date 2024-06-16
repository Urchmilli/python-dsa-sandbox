#Bubble sort, it is a popular sorting algorithm
#-> The time complexity is O(n**2) -> Quadratic 
#-> Space complexity is O(1) -> Constant time


def bubble_sort(element):
    size = len(element)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if element[j] > element[j+1]:
                temp = element[j]
                element[j] = element[j+1]
                element[j+1] = temp
                swapped = True

        if not swapped:
            break   
if __name__ == "__main__":
    element_one = [5,9,2,1,67,34,88,34]
    element_two = ["mona", "dhaval", "aamir", "tina", "chang"]
    
    bubble_sort(element_one)
    bubble_sort(element_two)
   
    print(element_one)
    print(element_two)
    
