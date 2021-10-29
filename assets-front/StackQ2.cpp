#include<iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {

        vector<string> res;
        int next = 1;
        for(int t: target){
            while(t != next) res.push_back("Push"), res.push_back("Pop"), next ++;
            res.push_back("Push"), next ++;
        }
        return res;
    }
};
int main()
{
    return 0;
}
