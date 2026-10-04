class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target == nums[mid]:
                return True
            if nums[left]<nums[mid]:#left subarray is sorted
                if target>nums[mid] or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            elif nums[left]>nums[mid]:#
                if target>nums[right] or target<nums[mid]:
                    right=mid-1 
                else:
                    left=mid+1
            else:
                left+=1
        return False
