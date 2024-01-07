
def searchInsert( nums, target):
    l,r=0,len(nums)-1
    i=0
    while(l<=r):
        midIndex = int((l+r)/2)
        print(nums[midIndex] == target)
        if(nums[midIndex] == target):
            return midIndex
        elif nums[midIndex]<target:
            l=midIndex +1
        else:
            r = midIndex-1
        
        # i+=1
        if(i==3):
            break
    
    return l+1  

nums =[1,3,5,6]
print(searchInsert(nums, 2))

