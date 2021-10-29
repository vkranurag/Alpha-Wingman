#include <iostream>
#include <queue>
using namespace std;

int main() {
    int x;
    cin>>x;
    while(x--)
    {
        int a,b,temp;
        priority_queue<int>pq;
        cin>>a>>b;
        for (int i = 0; i< a; i++) 
        {
            cin>>temp;
            pq.push(temp);
        }
        int hits=0;
        while(pq.top()!=0 && b>0)
        {
            hits++;
            temp=pq.top();
            b-=temp;
            pq.pop();
            pq.push(temp/2);
        }
        if(b>0)
        cout<<"Evacuate"<<endl;
        else
        cout<<hits<<endl;
    }
    return 0;
}
