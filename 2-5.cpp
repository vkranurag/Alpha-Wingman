#include <iostream>
#include <iomanip>
using namespace std;
class tollBooth
{
private:
unsigned int car;
double cash;
public:
tollBooth()
{
car=0;
cash=0;
}
void payingCar()
{
car++;
cash+=0.50; }
void nonpayCar()
{
car++;
}
void display() const
{
cout<<"\nTotal number of cars : "<<car<<endl;
cout<<"Total amount of cash : "<<cash<<endl; }
};
int main()
{
tollBooth t;
int c=1;
while(c<3) { cout <<"\n1. Paying Car\n2. Non-Paying Car\n3. Exit";
cout<<"\nEnter your choice: ";
cin>>c;
switch(c) {
case 1: t.payingCar();
break;
case 2: t.nonpayCar();
break;
case 3: t.display();
exit(0);
default:
cout<<"Invalid Choice!";
break; } }
return 0; }