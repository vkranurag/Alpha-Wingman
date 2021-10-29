#include <iostream>
using namespace std;
class time
{
int hr, min, sec;
public:
time()
{
hr=0;
min=0;
sec=0;
}
time(int h, int m, int s) {
hr=h;
min=m;
sec=s; }
void display()
{
cout<<hr<<":"<<min<<":"<<sec<<endl; }
void add(time x,time y) {
sec = x.sec + y.sec;
min = x.min + y.min;
hr = x.hr + y.hr;
if(sec>=60) {
min += sec/60;
sec = sec%60; }
if(min >= 60) {
hr += min/60;
min = min%60; } }
void add(time x) {
sec=sec+x.sec;
min=min+x.min;
hr=hr+x.hr;
if(sec >= 60) {
min += sec/60;
sec = sec%60; }
if(min >= 60) {
hr += min/60;
min = min%60; } }
};
int main()
{
time x(1,2,3), y(2,3,4), t;
cout<<"First output: "<<endl; x.display();
cout<<"Second output: "<<endl; y.display();
cout<<"Final output: "<<endl; t.add(x,y);
t.display();
return 0; }