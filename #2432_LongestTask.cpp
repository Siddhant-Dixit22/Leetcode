#include <vector>

using namespace std;

class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) {
        int maxID = logs.at(0).at(0), maxTime = logs.at(0).at(1), currTime;

        for (size_t i = 0; i < logs.size() - 1; ++i) {
            currTime = logs.at(i + 1).at(1) - logs.at(i).at(1);
            if (currTime > maxTime) {
                maxTime = currTime;
                maxID = logs.at(i+1).at(0);
            } else if (currTime == maxTime) {
                if (logs.at(i + 1).at(0) < maxID) {
                    maxID = logs.at(i + 1).at(0);
                }
            } else {
                continue;
            }
        }

        return maxID;
    }
};