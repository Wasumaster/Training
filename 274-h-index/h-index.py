class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0

        for indx, citation in enumerate(citations):
            rank = indx + 1

            if citation >= rank:
                h_index = rank
            else:
                break
        return h_index        
        