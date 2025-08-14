from collections import defaultdict

# Test case
nums = [4,1,-1,2,-1,2,3]
k = 2

# Function
def topKFrequent(nums, k):
    count = defaultdict(int)
    frequency = [[] for j in range(len(nums)+1)]
    for i in nums:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    for n,c  in count.items():
        frequency[c].append(n)

    res=[]
    for i in range(len(frequency)-1,0,-1):
        for n in frequency[i]:
            res.append(n)
            if len(res)==k:
                return res

# Function tested
print(topKFrequent(nums,k))
