#include<iostream>
using namespace std;
class solid
{
private:
float v;
public:
void volume(int s) { v = s*s*s; }
void volume(float r) { v = (4/3)*3.14*r*r*r; }
void volume(float r, float h) { v = 3.14*r*r*h; }
void volume(int l, int b, int h) { v=l*b*h; }
void display()
{
cout<<v<<endl; } }S;
int main()
{
int s,l,b,rh;
float r,cr,ch;
cout<<"Enter the side of the cube : ";
cin>>s;
cout<<"\nEnter the radius of the Sphere : ";
cin>>r;
cout<<"\nEnter the radius and height of the Cylinder : ";
cin>>cr>>ch;
cout<<"\nEnter the length, breadth and height of the Rectangular Box : ";
cin>>l>>b>>rh; S.volume(s);
cout<<"\nVolume of Cube is : "; S.display();
S.volume(r);
cout<<"Volume of Sphere is : "; S.display();
S.volume(cr,ch);
cout<<"Volume of Cylinder is : "; S.display();
S.volume(l,b,rh);
cout<<"Volume of Rectangular Box is : ";
S.display();
}