#include <vector>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double max = 0, window = 0;
        int n = nums.size();
        for (int i = 0; i < k; i++) {
            window += nums[i];
        }
        max = window;

        for (int j = k; j < n; j++) {
            window += nums[j] - nums[j - k];
            max = std::max(max, window);
        }

        return max/k;
    }
};