#include <iostream>
#include <math.h>
using namespace std;
class Complex
{
private:
float r;
float i;
public:
Complex()
{ r = 0; i = 0; }
void input()
{
cout << "Enter the real and imaginary part of the Complex Number : ";
cin >> r;
cin >> i; }
Complex operator+(Complex y) {
Complex t; t.r = r + y.r; t.i = i + y.i;
return t; }
Complex operator*(Complex y) {
Complex t; t.r = r * y.r - i * y.i; t.i = r * y.i + i * y.r;
return t; }
Complex operator-(Complex y) {
Complex t; t.r = r - y.r; t.i = i - y.i;
return t; }
Complex operator/(Complex y) {
Complex t; t.r=(((r)*(y.r))+((i)*(y.i)))/(pow(y.r,2)+pow(y.i,2));
t.i=(((r)*(i))-((r)*(y.i)))/(pow(y.r,2)+pow(y.i,2));
return t; }
void display()
{
cout<< r << " + " << i << "i" << endl; }
};
int main()
{
Complex x, y, z; x.input();
y.input();
z = x + y;
cout<<"\nAddition : "; z.display();
z = x - y;
cout<<"\nSubtraction : ";
z.display();
z = x * y;
cout<<"\nMultiplication : "; z.display();
z = x / y;
cout<<"\nDivision : "; z.display();
return 0; }