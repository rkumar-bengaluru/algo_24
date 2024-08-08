import java.util.*;
import java.util.stream.IntStream;

public class Solution {

    public long max_area_streams(int[] heights) {
       
        long v =  IntStream.range(0, heights.length) // Create a stream of indexes (0 to length-1)
        .mapToLong(i -> IntStream.range(i + 1, heights.length) // Inner stream for each index, starting from i+1 to avoid duplicates
                .mapToLong(j -> Math.min(heights[i], heights[j]) * (j - i)) // Calculate area for each pair
                .max().orElse(0)) // Get the maximum area from the inner stream or 0 if no elements
        .max().orElse(0); // Get the maximum area from the outer stream or 0 if no elements
        
        return v;
    }

    public int max_area(List<Integer> driver) {
        int maxArea = 0;
        int left = 0;
        int right = driver.size() - 1;
        while (left < right) {

            int length = (right - left);
            int breadth = Math.min(driver.get(left), driver.get(right));
            int area = length * breadth;
            maxArea = Math.max(area, maxArea);
            if (driver.get(right) > driver.get(left)) {
                left += 1;
            } else {
                right -=1;
            }
        }
        return maxArea;
    }
    public static void main(String[] args) {
        Solution s= new Solution();
        Integer[] driver = {2,3,4,5,18,17,6};
        int area = s.max_area(Arrays.asList(driver));
        System.out.println(String.format("max area is %d", area));
        int[] d = {2,3,4,5,18,17,6};
        long v = s.max_area_streams(d);
        System.out.println(String.format("max area is %d", v));
    }
}