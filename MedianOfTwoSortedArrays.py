class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        Len = nums1_len + nums2_len
        mid1 = (Len+1)//2-1
        mid2 = Len//2
        cur1 = 0
        cur2 = 0
        new_array = []
        while (cur1 < nums1_len) and (cur2 < nums2_len):
            if nums1[cur1] < nums2[cur2]:
                new_array.append(nums1[cur1])
                cur1 += 1
            else:
                new_array.append(nums2[cur2])
                cur2 += 1
        if cur1 == nums1_len:
            new_aray.extend(nums2[cur2 :])
        if cur2 == nums2_len:
            new_array.extend(nums1[cur1 :])
        return (new_array[mid1]+new_array[mid1])/2

print(max([1,2,3,]))