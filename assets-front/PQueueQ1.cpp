#include <iostream>
#include <queue>
using namespace std;
int main()
{
    priority_queue<vector<int>> pq;
    int a,n;
    cin>>a>>n;
    while (a--)
    {
        vector<int> v;
        for(int i=0;i<n;i++)
        {
            int x;
            cin>>x;
            v.push_back(x);
        }
        pq.push(v);
    }
    for(int i=0;i<pq.top().size();i++)
    cout<<pq.top()[i]<<" ";
    return 0;
}