public boolean arrayFront9(int[] nums) {
    int n = 0;
    
    while(n < nums.length && n < 4) {
        if(nums[n] == 9)
            return true;

        n++;
    }

    return false;
}
