/*
[AC 05/04/2024]
605. Can Place Flowers
Array / String
https://leetcode.com/problems/can-place-flowers/
*/

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int placed = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                boolean left = (i == 0 || flowerbed[i - 1] == 0);
                boolean right = (i == flowerbed.length - 1 || flowerbed[i + 1] == 0);
                if (left && right) {
                    flowerbed[i] = 1;
                    placed++;
                    if (placed >= n)
                        return true;
                }
            }
        }
        return placed >= n;
    }
}