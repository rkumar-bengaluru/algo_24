public class Solution {
    public boolean valid_mountain(int[] driver) {

        if (driver.length < 3) {
            return false;
        }
        int i = 0;
        while (i < driver.length) {
            if (driver[i] <= driver[i-1]) {
                break;
            }
            i += 1;
        }
        // check if i has reached to end, or i is equal to 1
        if (i == driver.length || i == 1) {
            return false;
        }
        while (i < driver.length) {
            if (driver[i] >= driver[i-1]) {
                break;
            }
            i += 1;
        }
        return i == driver.length;
    }
}