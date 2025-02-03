#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;
        int currNum = 0;
        int majorNum = 0;
        
        for (int i = 0; i < static_cast<int>(nums.size()); ++i){
            count = 0;
            currNum = nums.at(i);

            for(int x : nums){
                if (x == currNum){
                    ++count;
                }
            }

            if (count > static_cast<int>(nums.size() / 2)){
                return currNum;
            }

            if (count > maxCount){
                maxCount = count;
                majorNum = currNum;
            }
        }

        return majorNum;
    }
};