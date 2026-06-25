class Solution {
    public int[] twoSum(int[] nums, int target) {

        //   for i in range(len(nums)):
        //     for j in range(i+1,len(nums)):
        //         if nums[i]+ nums[j] ==target and i!=j:
        //             return [i,j]

    
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]+ nums[j] == target )
                {
                    return new int[]{i,j};
                } 
            }
        }
        return new int[0];
    }
    }   
    

