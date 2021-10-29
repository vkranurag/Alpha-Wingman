#include <iostream>
#include <set>

using namespace std;
int main()
{
    set<pair<int, string>> s = {{1, "1-9"}, {30, "21-40"}, {25, "21-40"}, {60, "41-60"}, {75, "61-80"}, {41, "41-60"}};
    multiset<string> sc;
    set<string> age = {"1-9", "10-20", "21-40", "41-60", "61-80", "81-100"};
    for (auto it = s.begin(); it != s.end(); ++it)
    {
        cout << (*it).first << " -category " << (*it).second << endl;
    }
    cout << endl;
    for (auto it = s.begin(); it != s.end(); ++it)
    {
        sc.insert((*it).second);
    }
    for (string i : age)
    {
        cout << i << " number of people " << sc.count(i) << endl;
    }
    return 0;
}