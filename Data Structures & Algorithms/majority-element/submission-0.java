class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();
        int maxNo = 0, maxCount=0;
        for(int num:nums){
            count.put(num, count.getOrDefault(num,0)+1);//basically checking if the key(num) is present in the count map.
            if(count.get(num)>maxCount){
                maxNo = num;
                maxCount=count.get(num);
            }
        }
        return maxNo;
    }
}