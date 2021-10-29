#include <iostream>
#include <string.h>
#include <cmath>
#include <stdio.h>
using namespace std;
class account
{
protected:
char cn[20];
int an;
char t;
int b;
public:
account()
{
strcpy(cn, " ");
an = 0; t = ' '; b = 0; }
void input()
{
cout << "\nEnter customer name: ";
cin >> cn;
cout << "Enter account number: ";
cin >> an;
cout << "Enter the type of account(s or c): ";
cin >> t;
cout << "Enter balance: ";
cin >> b; }
void deposit()
{
int a;
cout << "\nEnter the amount to deposit: ";
cin >> a; b = b + a; }
void display()
{
cout << "\nCustomer Name : " << cn;
cout << "\nAccount Number : " << an;
cout << "\nType : " << t;
cout << "\nBalance : " << b << endl; }
};
class sav_acct : public account
{
int i;
public:
int comp_int()
{
int time1, rate1;
rate1 = 10;
cout << "\nEnter the time";
cin >> time1; i = b * pow(1 + rate1 / 100.0, time1) - b;
return i; }
void ubal()
{ b = b + comp_int();
}
void withdraw()
{
int a;
cout << "\nEnter the amount to be withdrawn: ";
cin >> a;
if (b >= a) { b = b - a; }
else
cout << "\nThe amount cannot be withdrawn"; }
};
class cur_acct : public account
{
int p;
public:
int mbal()
{
int ret1 = 1;
if (b <= 500) { p = 50; b = b - p;
ret1 = 0; }
else
cout << "\nNo penality imposed";
return ret1; }
void withdraw()
{
int a;
cout << "\nEnter the amount to be withdrawn: ";
cin >> a;
int k = mbal();
if (k == 1)
if (b >= a) b = b - a;
else
cout << "\nThe amount cannot be withdrawn"; }
};
int main()
{
cur_acct c;
sav_acct s1; c.input();
c.display();
c.deposit();
c.display();
c.withdraw();
c.display();
s1.input();
s1.display();
s1.deposit();
s1.display();
s1.withdraw();
s1.display();
}