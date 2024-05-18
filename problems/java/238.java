/*
[AC 05/07/2024]
238. Product of Array Except Self
Array / String
https://leetcode.com/problems/product-of-array-except-self/
*/

class Solution {
    // This solution runs in O(n) time with O(1) aux. space
    // ans[i] = pref[i] * suff[i]
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, 1);
        int curr = 1;

        for (int i = 0; i < n; i++) {
            ans[i] *= curr;
            curr *= nums[i];
        }

        curr = 1;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] *= curr;
            curr *= nums[i];
        }

        return ans;
    }
}