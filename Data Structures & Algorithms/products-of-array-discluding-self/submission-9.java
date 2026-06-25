class Solution {
    public int[] productExceptSelf(int[] nums) {
        
        // res=[]
        // pre=[]
        // for i in range(len(nums)):
        //             if i == 0:
        //                 pre.append(1)
        //             else:
        //                 pre.append(nums[i-1]*pre[i-1])
        // suf=[0]*len(nums)
        // for i in range(len(nums)-1,-1,-1):
        //     if i ==  len(nums)-1:
        //         suf[i]=1
        //     else:
        //         suf[i]=nums[i+1]*suf[i+1]
        // for i in range(len(nums)):
        //     res.append(pre[i]*suf[i])
        // return res

        int []pre=new int[nums.length];
        int []suf=new int[nums.length];
        int []res=new int[nums.length];

        for(int i=0;i<nums.length;i++)
        {
            if(i == 0 ){
                pre[i]=1;
            }
            else{
                pre[i]=nums[i-1] * pre[i-1];
            }
        }
        for(int i=nums.length-1;i>=0;i--)
        {
            if(i == nums.length-1 ){
                suf[i]=1;
            }
            else{
                suf[i]=nums[i+1] * suf[i+1];
            }
        }
        for(int i=0;i<nums.length;i++)
        {
            res[i]=pre[i] * suf[i];
        }
        return res;
    }
}  
