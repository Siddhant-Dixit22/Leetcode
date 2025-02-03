#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sum = 0;
        std::vector<int> output;

        for (int i = 0; i < nums.size(); ++i){
            int x = nums.at(i);
            for (int j = 0; j < nums.size(); ++j){
                if (i == j){
                    continue;
                }
                sum = x + nums.at(j);
                if (sum == target){
                    output = {i, j};
                }
            }
        }
        return output;
    }
};