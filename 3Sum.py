def threeSum(nums: list[int]) -> list[list[int]]:
    triplets = []
    visited = set()
    for i in range(len(nums)-1):
        val = nums[i]
        sum_dict = {}
        for j in range(len(nums)):
            if nums[j] not in visited:
                sum_dict[nums[j]] = -nums[j]-val
            if -nums[j]-val in sum_dict:
                triplets.append([val,  -nums[j]-val, nums[j]])
            visited.add(val)
    return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

