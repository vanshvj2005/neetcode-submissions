class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        int i=0;
        int j = i+1;
        sort(nums.begin(),nums.end());
        while(j<n){
            if(nums[i] == nums[j]){
                return true;
            }
            i++;
            j++;
        }
        return false;
    }
};