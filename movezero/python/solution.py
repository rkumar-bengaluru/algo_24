from typing import List 

class Solution:
    '''
    Given an integer array nums, move all 0's to the end of it while maintaining the 
    relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example nums   = [0,1,0,3,12]
            output = [1,3,12,0,0]
    '''
    def move_zeroes(self, numbers: List[int]) -> List[int]:
        zeroIndex = 0
        for value in numbers:
            if value != 0:
                numbers[zeroIndex] = value 
                zeroIndex += 1
        while zeroIndex < len(numbers):
            numbers[zeroIndex] = 0
            zeroIndex += 1
        return numbers