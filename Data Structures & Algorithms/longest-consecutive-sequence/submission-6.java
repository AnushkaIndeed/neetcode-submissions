class Solution {
    public int longestConsecutive(int[] nums) {
       HashSet<Integer> set= new HashSet<>();
       //add elements to the hashset
       for(int num: nums){
        set.add(num);
       } 
       //set the integer that gives the final count
       int longest =0;
       //define a for loop
       for(int num: set){
        // it only starts if the sequence does not contain the previous number meaning it starts only if the number is the beginning for the sequence
       if(!set.contains(num-1)){
        int current= num;
        int length=1;
        // check if the current element has the next number in the set and then extend the length by 1 
        while(set.contains(current+1)){
            current++;
            length++;
        }
        //replace the longest counter with the value of length in short 
        longest= Math.max(longest, length);
       }
       }
       return longest;
    }
}
