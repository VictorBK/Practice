public boolean array123(int[] nums) {
    int current = 1;
    for(int n = 0; n < nums.length - 2; n++) {
        if(nums[n] == 1 && nums[n + 1] == 2 && nums[n + 2] == 3)
            return true;
    }
    return false;    
}
