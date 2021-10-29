#include <iostream>
#include <set>
using namespace std;

int main()
{
    multiset<int> s;
    int n,k,num,num1;
    cout<<"Enter the number of iterations required"<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cout<<"Enter the number to be inserted"<<endl;
        cin>>num;
        s.insert(num);
    }
    cout<<"Enter the number to be searched"<<endl;
    cin>>num1;
    k=s.count(num1);
    if(k>0)
    {
        cout<<"Number "<<num1<<" found "<<k<<" times in the set."<<endl;
    }
    else
    {
        cout<<"Number "<<num1<<" not found in the set."<<endl;
    }
    return 0;
}