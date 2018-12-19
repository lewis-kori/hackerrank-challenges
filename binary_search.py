def toTwenty():
    return range(1,21)
def toForty():
    return range(2,41,2)
def toOneThousand():
    return range(10,1001,10)


def numbers(arr,start_index,end_index,num):
    if end_index>=start_index:
        mid=start_index+(end_index-start_index)//2
        if(arr[mid==num]):
            return mid
        elif(arr[mid]>num):
            end_index=mid-1
            return numbers(arr,start_index,end_index,num)
        else:
            end_index=mid+1
            return numbers(arr,start_index,end_index,num)
    else:
        return -1
        
array=range(1,100)
start_index=0
end_index=len(array)-1
num=30
print(numbers(array,start_index,end_index,num))
