class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for num in nums:
            frequency[num]= frequency.get(num,0)+1
            
        sorted_items= sorted(
            frequency.items(),
            key=lambda x:x[1],
            reverse=True
        )
        result = [num for num, freq in sorted_items[:k] ]

        return result
