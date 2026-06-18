#optimal

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            low, high = 0, len(nums)-1
            first = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # search left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def find_last(nums, target):
            low, high = 0, len(nums)-1
            last = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1  # search right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [find_first(nums, target), find_last(nums, target)]
