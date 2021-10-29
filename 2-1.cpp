#include <iostream>
using namespace std;
class Complex
{
private:int r;
private:int i;
public:
void read()
{
cout<<"Enter the real and imaginary part of the complex number: ";
cin>>r>>i; }
void display()
{
cout<< r << " + " << i << "i" << endl; 
}
Complex add(Complex x, Complex y) 
{
Complex z; z.r=x.r+y.r; z.i=x.i+y.i;
return z; 
}
Complex mul(Complex x, Complex y) 
{
Complex z; z.r=x.r*y.r-x.i*y.i; z.i=x.r*y.i+x.i*y.r;
return z; 
}
};
int main()
{
Complex a, b, c; a.read();
b.read();
cout<<"\nAddition : "; c = a.add(a, b);
c.display();
cout<<"Multiplication : "; c = a.mul(a, b);
c.display();
return 0; 
}