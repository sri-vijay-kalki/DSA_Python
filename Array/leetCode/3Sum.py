def threeSum( nums):
    fList = []
    nums[:] = sorted(nums)
    for i, val in enumerate(nums):
        if i> 0 and val == nums[i-1]:
            continue
        
        l,r = i+1,len(nums)-1
        while(l<r):
            tsum = val+nums[l]+nums[r]
            if tsum==0:
                fList.append([val,nums[l],nums[r]])
                l+=1
                while(l<r and nums[l] == nums[l-1]):
                    l+=1
            elif tsum>0:
                r-=1
            else:
                l+=1
    return fList

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

