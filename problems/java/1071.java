/*
[AC 05/02/2024]
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
*/

class Solution {
    private boolean valid(String str1, String str2, int k) {
        int n1 = str1.length(), n2 = str2.length();
        if (n1 % k > 0 || n2 % k > 0) {
            return false;
        } else {
            String base = str1.substring(0, k);
            return str1.replace(base, "").isEmpty() && str2.replace(base, "").isEmpty();
        }
    }

    public String gcdOfStrings(String str1, String str2) {
        int n1 = str1.length(), n2 = str2.length();
        for (int i = Math.min(n1, n2); i >= 1; --i) {
            if (valid(str1, str2, i)) {
                return str1.substring(0, i);
            }
        }
        return "";
    }
}