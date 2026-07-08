class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> v ;
        int val;
        for(int i=0;i<nums.size();i++){
            val = target - nums[i];
            if( v.find(val) != v.end()){
                return {v[val],i};
            }
            v[nums[i]] =i;
        }


    }
};
