#include <string>

class Solution {
public:
    bool isPalindrome(int x) {
        std::string numStr = std::to_string(x);
        std::string palindromeStr = "";

        for (int i = numStr.size()-1; i >=0; --i){
            palindromeStr += numStr.at(i);
        }
        
        if (palindromeStr == numStr){
            return true;
        }
        else {
            return false;
        }
    }
};