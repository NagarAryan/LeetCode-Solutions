class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ar[]=new int [2];
        int c=0;
        for(int i=0;i<nums.length;i++)
        {
            for (int j=i+1;j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target)
                {  c=1;
                   ar[0]=i;
                    ar[1]=j;
                 break;
                }
            }
            if (c==1)
                break;
        }
        return ar;
        
    }
}