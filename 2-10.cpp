#include <iostream>
using namespace std;
class Incometax
{
public:
int t;
void disp(int sal) {
cout<<"Salary : "<<sal<<endl;
cout<<"Tax : "<<t<<endl; }
};
class Doctor
{
public:
int sal;
friend class Incometax;
Doctor(int s) {
sal=s; }
};
class Engineer
{
public:
int sal;
friend class Incometax;
Engineer(int s) {
sal=s; }
};
int main()
{
Doctor d(5000);
Engineer e(7000);
Incometax i; 
i.t=0.1*d.sal;
cout<<"Doctor \n"; i.disp(d.sal);
i.t=02*e.sal;
cout<<"Engineer \n"; i.disp(e.sal);
return 0; }