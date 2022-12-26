# return the unique element form the array
# 1,2,2,3,1,4,5
# 4 5
def freqMap(arr):
    freq={}           #building an frequency map
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq      # returning frequency map
def uniqueElements(arr):
    freq=freqMap(arr)
    count=0
    for i in arr:
        if(freq[i]==1):
            count+=1
    return count
print(uniqueElements([1,2,2,3,4,5,5]))
