"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

#test = [1,2,3,-3,1,1,1,4,2,-3]
test = [1,1,1]
k = 2

def subarraySum(nums, k):
    fixed_sum_dict = {0:1}
    counter = 0
    for i in range(len(nums)-1):
        nums[i+1]=nums[i+1]+nums[i]

    for i in range(len(nums)):

        # Se esiste una somma cumulativa precedente tale che
        # current_sum - previous_sum = k, allora abbiamo trovato
        # un sottovettore valido
        if nums[i] - k in fixed_sum_dict.keys():
            counter = counter + fixed_sum_dict[nums[i]-k]
        if nums[i] in fixed_sum_dict.keys():
            fixed_sum_dict[nums[i]] += 1
        else:
            fixed_sum_dict[nums[i]] = 1

    return counter
print(subarraySum(test,k))


### Idea

# Calcola somme cumulative di nums (modificando nums stesso).
# Usa un dizionario per contare quante volte è stata vista ciascuna somma cumulativa.
# Per ogni posizione i:
#    Guarda se c’è stata una somma cumulativa pari a prefix[i] - k.
#    Se sì, aumenta il contatore del numero di volte in cui quella somma è apparsa → questi sono sottovettori che finiscono in i e sommano a k.
#    Aggiorna il dizionario con la somma cumulativa corrente.

