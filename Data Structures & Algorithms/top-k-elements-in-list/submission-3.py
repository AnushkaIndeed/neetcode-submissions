#Bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        n= len(nums)
        for num in nums:
            frequency[num]= frequency.get(num,0)+1
        buckets= [[] for _ in range(n+1)]
        for num,freq in frequency.items():
            buckets[freq].append(num)
        result =[]
        for i in range( len(buckets) -1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
             return result

