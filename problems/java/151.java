/*
[AC 05/06/2024]
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
*/

class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        String reversed = "";
        
        for (int i = words.length - 1; i > 0; i--) {
            reversed += words[i] + " ";
        }

        return reversed + words[0];
    }
}