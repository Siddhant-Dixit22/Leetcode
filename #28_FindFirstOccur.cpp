#include <string>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        std::string currStr;
        if (haystack.size() >= needle.size()) {
            for (int i = 0; i < haystack.size() - (needle.size() - 1); ++i) {
                currStr = haystack.substr(i, needle.size());
                if (needle == currStr) {
                    return i;
                }
            }
        }
        return -1;
    }
};