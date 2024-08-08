from typing import List

class Solution:
    '''
    Given an array of integers arr, return true if and only if it is a valid mountain array.
    Recall that arr is a mountain array if and only if:
        arr.length >= 3
        There exists some i with 0 < i < arr.length - 1 such that
            arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
        
        Example 1:

        Input: arr = [2,1]
        Output: false

        Example 2:

        Input: arr = [3,5,5]
        Output: false

        Example 3:

        Input: arr = [0,3,2,1]
        Output: true
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        if arr[i] <= arr[i-1]:
            return False
        # check if increasing sequence
        while i < len(arr):
            if arr[i] <= arr[i-1]:
                break
            i += 1
        print(i,len(arr))
        # check if i reaches end then return False
        if i == len(arr):
            return False
        
        # check for decreasing sequence
        while i < len(arr):
            if arr[i] >= arr[i-1]:
                break
            i += 1
        # check if i reaches end then return False
        return i == len(arr)
