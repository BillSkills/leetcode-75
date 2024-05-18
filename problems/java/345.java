/*
[AC 05/05/2024]
345. Reverse Vowels of a String
Array / String
https://leetcode.com/problems/reverse-vowels-of-a-string/
*/

class Solution {
    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        ArrayList<Character> vowels = new ArrayList<>();

        for (char c : arr) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O'
                    || c == 'U') {
                vowels.add(c);
            }
        }

        int i = 0, j = vowels.size() - 1;
        for (char c : arr) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O'
                    || c == 'U') {
                arr[i] = vowels.get(j);
                j--;
            }
            i++;
        }

        return new String(arr);
    }
}