#given an array find out the first repeating element least index
# 3 2 1 5 2 6 8 3
# output 3

def freqMap(arr):
    freq={}           #building an frequency map
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq      # returning frequency map
def firstNonrepating(arr):
    freq=freqMap(arr)
    for i in arr:    # comparing array with frweq map and checking first no with count as 1
        if freq[i]==1:
            return i
    return -1
print(firstNonrepating([1,1,2,3,4,2,3]))
