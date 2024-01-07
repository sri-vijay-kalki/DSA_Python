def searchRange( nums, target):
    l = 0
    r = len(nums)-1
    fi,li =-1,-1
    while l<=r:
        m = (l+r)//2
        if nums[m] ==target:
            fi = m
            li = m
            break
        if target <nums[m]:
            r = m-1
        else:
            l = m+1
    print(fi, li)
    if fi != -1:
        while(nums[fi-1]==target and fi>0):
            fi-=1
        while(li<len(nums)-1 and nums[li+1]==target):
            li+=1
    return [fi, li]

nums = [1]
print(searchRange(nums,1))