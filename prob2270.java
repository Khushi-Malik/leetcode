/*2270. Number of Ways to Split Array */

public class prob2270 {

    /**You are given a 0-indexed integer array nums of length n.
    nums contains a valid split at index i if the following are true:
    The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
    There is at least one element to the right of i. That is, 0 <= i < n - 1.
    Return the number of valid splits in nums.
    */
    public int waysToSplitArray(int[] nums) {
        int n = nums.length;
        long[] sums = new long[n];
        sums[0] = nums[0];
        for(int i = 1; i < n; i++){
            sums[i] = sums[i-1] + nums[i];
        }
        
        int valid = 0;
        long totalSum = sums[n - 1];
        for(int i = 1; i < n; i++){
            long leftSum = sums[i - 1];
            long rightSum = totalSum - leftSum;
            if (leftSum >= rightSum){
                valid++;
            }
        }

        return valid;
    }

    public static void main(String[] args) {
        prob2270 obj = new prob2270();

        int[] nums = {10,4,-8,7};
        int result = obj.waysToSplitArray(nums);

        System.out.println(result);
    }
}
