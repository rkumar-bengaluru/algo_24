import java.util.List;
import java.util.Arrays;
import java.util.Collections;
class Solution {

    public int boatsToSavePeople(List<Integer> peopleWeights, int limit) {
        Collections.sort(peopleWeights);
        int noOfBoats = 0;
        int left = 0;
        int right = peopleWeights.size() -1;
        while (left < right) {
            noOfBoats += 1;
            int sum = peopleWeights.get(left) + peopleWeights.get(right);
            if (sum == limit || sum < limit) {
                left += 1;
                right -= 1;
            } else if (sum > limit ) {
                right -= 1;
            }
        }
        if (left == right) {
            noOfBoats += 1;
        }
        return noOfBoats;
    }   

    public static void main(String[] args) {
        List<Integer> weights = Arrays.asList(3,2,2,1);
        int limit = 3;
        Solution s = new Solution();
        int got = s.boatsToSavePeople(weights, limit);
        int want = 3;
        if (got != want) {
            System.err.println("test failed...");
        }

    }
}