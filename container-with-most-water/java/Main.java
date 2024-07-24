import java.util.*;

public class Main {

    public static int max_area(List<Integer> driver) {
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
        Integer[] driver = {2,3,4,5,18,17,6};
        int area = max_area(Arrays.asList(driver));
        System.out.println(String.format("max area is %d", area));
    }
}