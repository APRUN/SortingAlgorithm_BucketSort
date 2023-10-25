def InsertionSort(array,start,end):
    for index in range(start+1,end):
        key=array[index]
        j=index-1
#Moving elements to correct position
        while j>=start and array[j]>key:
            array[j],array[j+1]=array[j+1],array[j]
            j=j-1
#Returnng the final array after sorting
    return array[start:end+1]

def BucketSort(array,size):
    min_value=min(array)
    max_value=max(array)
    
    bucket_size=int((max_value-min_value)/size)
    buckets=[]*size
    
    for n in array:
        index = int((n - min_value) / bucket_size)
        if index != size:
            buckets[index].append(n)
        else:
            buckets[index - 1].append(n)
        sorted_arr = []
    for bucket in buckets:
        InsertionSort(bucket)  # You can use any sorting algorithm here
        sorted_arr.extend(bucket)
a=[2,9,8,6,4,2,1,56]
BucketSort(a,len(a))
print(a)

        