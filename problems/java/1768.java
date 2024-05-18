/*
[AC 05/01/2024]
1768. Merge Strings Alternately
Array / String
https://leetcode.com/problems/merge-strings-alternately/
*/

class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] w1 = word1.toCharArray();
        char[] w2 = word2.toCharArray();
        char[] merge = new char[w1.length + w2.length];

        int i = 0, j = 0;
        while (i < w1.length || i < w2.length) {
            if (i < w1.length) {
                merge[j] = w1[i];
                j++;
            }
            if (i < w2.length) {
                merge[j] = w2[i];
                j++;
            }
            i++;
        }

        return new String(merge);
    }
}