class Solution:
    def mergeSortedArray(nums1, m, nums2, n):
        last = m + n - 1

        # Merge nums1 and nums2 starting from the end
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # If there are remaining elements in nums2
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n - 1, last - 1

# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

Solution.mergeSortedArray(nums1, m, nums2, n)
print(nums1)