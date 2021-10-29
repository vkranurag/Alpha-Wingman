#include<iostream>
using namespace std;
class Rectangle
{
private:
int length,breadth;
public:
Rectangle()
{
length=0;
breadth=0; }
~Rectangle()
{
cout<<"\nDestructor function called."; }
Rectangle(int l,int b)
{
length=l;
breadth=b; }
Rectangle(const Rectangle &r) {
length=r.length;
breadth=r.breadth; }
void Area()
{
cout<<"\nArea of rectangle :"<<length*breadth; 
}
};
int main()
{
int l,b;
cout<<"Enter the length and breadth of the rectangle : ";
cin>>l>>b;
Rectangle x,y(l,b),z(y);
x.Area();
y.Area();
z.Area();
return 0; 
}