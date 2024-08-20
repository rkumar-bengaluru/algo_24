package movezero.javamz;

/**
 *  Given an integer array nums, move all 0's to the end of it while maintaining the 
    relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example nums   = [0,1,0,3,12]
            output = [1,3,12,0,0]
 */
public class MoveZeroSolution {
    public void movezero(int[] nums) {
        int zeroIndex = 0;
        for (int i =0; i < nums.length; i++) {
            if (nums[i] == 0) {
                nums[zeroIndex] = nums[i];
                zeroIndex++;
            }
        }
        while (zeroIndex < nums.length) {
            nums[zeroIndex] = 0;
            zeroIndex++;
        }
    }
}
