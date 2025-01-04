
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class prob1930 {
    /**Given a string s, return the number of unique palindromes of length 
     * three that are a subsequence of s.
     * Note that even if there are multiple ways to obtain the same subsequence, 
     * it is still only counted once.
     * A palindrome is a string that reads the same forwards and backwards.
     * 
     * A subsequence of a string is a new string generated from the original string 
     * with some characters (can be none) deleted without changing the relative 
     * order of the remaining characters.
     * 
     * For example, "ace" is a subsequence of "abcde". 
     * 
     * 
     * COMPLEXITIY O(N^3)*/
    public int countPalindromicSubsequence(String s) {
        Set<String> set = new HashSet<>();
        
        int n = s.length();
        for(int i=0; i < n; i++){
            for(int j=0; j < i; j++){
                for(int k=0; k < j; k++){
                    if(i!=j && j!=k && k!=i){
                        String temp = "" + s.charAt(k) + s.charAt(j) + s.charAt(i);
                        if(isPalindrome(temp)){
                            set.add(temp);
                        }
                    }
                }
            }
        }
        return set.size();
    }

    /** COMPLEXITY O(N) */
    public int countPalindromicSubsequence2(String s) {
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        
        for (int i = 0; i < s.length(); i++) {
            int curr = s.charAt(i) - 'a';
            if (first[curr] == - 1) {
                first[curr] = i;
            }
            last[curr] = i;
        }
        
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) {
                continue;
            }
            
            Set<Character> between = new HashSet<>();
            for (int j = first[i] + 1; j < last[i]; j++) {
                between.add(s.charAt(j));
            }
            
            ans += between.size();
        }
        
        return ans;
    }

    public boolean isPalindrome(String s){
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != s.charAt(n - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        prob1930 obj = new prob1930();

        String s = "bbcbaba";
        int result = obj.countPalindromicSubsequence2(s);

        System.out.println(result);
    }
}
