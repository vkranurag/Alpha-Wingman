#include<iostream>
using namespace std;
class Counter
{
private:
int count;
public:
void init()
{
count=0; }
void display()
{
cout<<"Number of Count is: "<<count<<endl; }
void cnt()
{
count++;
}
};
int main()
{
Counter x; x.init();
int c=1;
while(c<3) {
cout<<"\n1. Count\n2. Display\n3. Exit\n";
cout<<"\nEnter Your choice: ";
cin>>c;
switch(c) {
case 1: x.cnt();
break;
case 2: x.display();
break;
case 3:
break;
default:
cout<<"Invalid choice";
} } }