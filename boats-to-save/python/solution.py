from typing import List

class Solution:
    def boats_to_save(self,people_weights : List[int], limit: int) -> int:
        '''
        You are given an array people where people[i] is the weight of the ith person, and an 
        infinite number of boats where each boat can carry a maximum weight of limit. Each boat 
        carries at most two people at the same time, provided the sum of the weight of those people 
        is at most limit.

        Return the minimum number of boats to carry every given person.
        '''
        noOfBoats = 0
        people_weights.sort()
        left = 0
        right = len(people_weights)
        while left < right:
            weights = people_weights[left] + people_weights[right -1]
            noOfBoats += 1
            if weights == limit:
                right -= 1
                left += 1
            elif weights > limit:
                right -= 1
            elif weights < limit:
                right -=1
                left += 1
        if left == right - 1:
            noOfBoats += 1
        return noOfBoats

       
       
    