class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common = counts.most_common(k)

        result = []
        for number, count in most_common:
            result.append(number)
        
        return(result)