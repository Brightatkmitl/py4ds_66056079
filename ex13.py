def calculateSum(input):
    total = 0
    for i in input:
        total = total +1
    return total
def calculateProduct(input):
    total = 0
    for i in input:
        total = total*i
    return total

def average(input):
    total = 0
    for i in input:
        total = total + i
        lens = len(input)
    return total / lens

def median(input):
    input = input.sort()
    # input_sort = input.sort()
    input_len = len(input)
    if input_len == 0:
        return None
    elif input_len % 2 == 0:
        index = input_len // 2
        return (input_sort[index] + input_sort[index - 1]) / 2
    else:
        index = input_len // 2
        return input_sort[index]

















if __name__ == '__main__':
    # calculateSum
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateSum([1, 3, 5, 7, 9]) == 25)
    print("--------------------")

    # calculateProduct
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)
    print("--------------------")




    # average
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)
    print("--------------------")
    #
    # median
    print(median([]) is None)  # Comparison with None performed with equality operators
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)
    #
    # # # mode
    # # print(mode([]) is None)  # Comparison with None performed with equality operators
    # # print(mode([1, 2, 3, 4, 4]) == 4)
    # # print(mode([1, 1, 2, 3, 4]) == 1)
#%%
