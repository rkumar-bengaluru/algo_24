class Solution:
    def __init__(self, driver) -> None:
        self.driver = driver

    def max_area(self):
        maxArea = 0
        left = 0
        right = len(self.driver) -1
        while(left < right):
            # compute the area which is length * height
            area = (right - left) * min(self.driver[left], self.driver[right])
            maxArea = max(area,maxArea)
            if self.driver[left] > self.driver[right]:
                right -= 1
            else:
                left +=1

        return maxArea


if __name__ == "__main__":
    driver = [2,3,4,5,18,17,6]
    sol = Solution(driver)
    max_area = sol.max_area()
    print('max area is {}'.format(max_area))