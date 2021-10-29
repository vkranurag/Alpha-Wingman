#include<conio.h>
#include<iostream>
using namespace std;
class DM
{ public:
 float meter;
 void getdata()
 {
 cout<< "enter distance in meters and centimeters :" ;
 cin>> meter ;
 }
 friend void add();
} inp1;
class DB
{ public:
 float inch;
 void getdata()
 {
 cout<< "enter distance in feets and inches :" ;
 cin>> inch ;}
 friend void add();} 
inp2;
void add()
{ double a,res;
 a = inp1.meter * 39.37;
 res = a + inp2.inch;
 cout<< " total inches = " << res <<endl;
 a = inp2.inch / 39.37;
 res = a + inp1.meter;
 cout<< " total meters = " << res << endl;}
 
int main()
{ inp1.getdata();
 inp2.getdata();
 add();
 return 0;
}