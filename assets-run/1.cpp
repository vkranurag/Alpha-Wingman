#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> s;
    int n,k,num1,num2;
    cout<<"Enter number of iterations required: ";
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cout<<"1.Insert "<<endl;
        cout<<"2.Search "<<endl;
        cout<<"3.Exit "<<endl;
        cout<<"Enter your choice: ";
        cin>>k;
        if(k==1)
        {
            cout<<"Enter the number to be inserted"<<endl;
            cin>>num1;
            if(s.find(num1)!=s.end())
            {
                cout<<"number "<<num1<<" already there in the set "<<endl;
            }
            else
            {
                s.insert(num1);
                cout<<"number "<<num1<<" inserted successfully"<<endl;
            }
        }
        else if(k==2)
        {
            cout<<"Enter the number to be searched"<<endl;
            cin>>num2;
            if(s.find(num2)!=s.end())
            {
                cout<<"number "<<num2<<" found "<<endl;
            }
            else
            {
                cout<<"number "<<num2<<" not found"<<endl;
            }
        }
        else if(k==3)
        {
            cout<<"Exiting!";
            exit(0);
        }
    }

    return 0;

}