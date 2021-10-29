#include <iostream>
#include <queue>
#include <array>
using namespace std;

queue<int> queueone, queuetwo;

void check()
{
    if(queueone.empty())
    cout<<"Queue is empty"<<endl;
    else 
    cout<<"Queue is not empty"<<endl;
}

int main()
{
    check();
	std::queue<int> queueone, queuetwo;
    queueone.emplace(3);
    queueone.emplace(6);
    queueone.emplace(7);
	queueone.swap(queuetwo);
   while(!queuetwo.empty())
    {
        cout<<queuetwo.front()<<" ";
        queuetwo.pop();
    }
    cout<<endl;
    queueone.push(10);
    queueone.push(20);
    queuetwo.push(30);
    queuetwo.push(40);
    queuetwo.push(50);
    queueone.swap(queuetwo);
    int l=queueone.size();
    for(int i=0;i<l;i++)
    {
        queuetwo.push(queueone.front());
        queueone.pop();
    }
    cout<<"Size of queuetwo is: "<<queuetwo.size()<<endl;
    cout<<"Size of queueone is: "<<queueone.size()<<endl;
    array<int,10> a;
    for (int i=0;i<10;i++)
    {
        cin>>a[i];
        a.back()=a[i];
    }
    return 0;
}
