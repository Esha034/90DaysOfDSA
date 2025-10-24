from typing import List

class Solution:
    def paint(self, A: int, B: int, C: List[int]) -> int:
        n=len(C)
        def isPossible(C: List[int], time: int) -> bool:
            painters = 1
            total = 0
            for i in range(n):
                if total + C[i] <=time:
                    total += C[i]
                else:
                    painters += 1
                    total = C[i]
                    if painters > A:
                        return False
            return True
        
        low = max(C)
        high = sum(C)
        res = high
        
        while low <= high:
            mid = low + (high - low) // 2
            if isPossible(C,mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return (res * B) % 10000003
