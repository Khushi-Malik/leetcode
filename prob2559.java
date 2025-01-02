/* Count Vowel Strings in Ranges */

import java.util.List;

class prob2559{

     /**
     * Finds the number of strings in the range specified by queries that start 
     * and end with a vowel.
     *
     * @param words   an array of strings
     * @param queries a 2D array of integers representing query ranges
     * @return an array of integers where each value is the result of a query
     */
    public int[] vowelStrings(String[] words, int[][] queries) {
        // THIS METHOD EXCEEDED TIME LIMIT 
        List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');
        int[] output = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int[] query = queries[q];
            int count = 0;
            for (int i = query[0]; i <= query[1]; i++) {
                String word = words[i];
                if (vowels.contains(word.charAt(0)) && vowels.contains(word.charAt(word.length() - 1))){
                    count++;
                }
            }   
            output[q] = count;
        }
        return output;
    }

    public int[] vowelStrings2(String[] words, int[][] queries) {
        int[] prefixSum = new int[words.length];
        List<Character> vowels = List.of('a', 'e', 'i', 'o', 'u');
        int[] output = new int[queries.length];

        int count = 0;
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (vowels.contains(word.charAt(0)) && vowels.contains(word.charAt(word.length() - 1))){
                count++;
            }
            prefixSum[i] = count;
        }

        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int startSum = 0;
            if (query[0] != 0) {
                startSum = prefixSum[query[0] - 1];
            }

            output[i] = prefixSum[query[1]] - startSum;
        }

        return output;
    }

    public static void main(String[] args) {
        prob2559 obj = new prob2559();

        // Test case
        String[] words = {"apple", "orange", "idea", "umbrella", "echo", "dog"};
        int[][] queries = {{0, 2}, {1, 4}, {3, 5}};
        
        // Call the method
        int[] results = obj.vowelStrings(words, queries);
        
        // Print results
        for (int result : results) {
            System.out.println(result);
        }
    }

}
    