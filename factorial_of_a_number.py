n = 30

def fact(n):

    #declare the array and initialize the array
    array = [0]*10000

    # A variable to track the size of the array
    size = 1
    # set the first element in the array to 1
    array[0] = 1

    carry = 0
    # Loop through all the numbers
    for i in range(2,n+1):

        j = 0
        while(j < size):

            result = (array[j] * i) + carry
            array[j] = result % 10
            carry = result // 10
            j += 1

        while(carry > 0):
            array[size] = carry % 10
            carry = carry // 10
            size += 1
    # reverse the array and
    return ''.join(map(str,array[::-1][len(array)-size:]))


fac_n = fact(n)
print(len(fac_n) - len(fac_n.rstrip('0')))
