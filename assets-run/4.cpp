#include <iostream>
#include <map>
using namespace std;
int data;

void print_map(map<int, string> m, map<int, string> m2)
{
    map<int, string>::iterator itr;
    map<int, string>::iterator itr1;
    if (data != 1000)
    {
        for (itr = m.find(data - 1); itr != m.find(data + 2); ++itr)
        {
            if ((*itr).first != data)
            {
                cout << (*itr).second << "\n";
                for (itr1 = m2.begin(); itr1 != m2.end(); ++itr1)
                {
                    if ((*itr).first == (*itr1).first)
                    {
                        cout << (*itr1).second;
                        break;
                    }
                }
                cout << endl;
            }
        }
    }
    else
    {
        cout << "Your Input is wrong!!!!";
    }
}

void finder(map<int, string> temp, map<int, string> temp1, string s)
{
    for (auto itr = temp.begin(); itr != temp.end(); ++itr)
    {
        if (s == (*itr).second)
        {
            data = (*itr).first;
            for (auto itr1 = temp1.begin(); itr1 != temp1.end(); ++itr1)
            {
                if ((*itr).first == (*itr1).first)
                {
                    cout << (*itr1).second << endl;
                    break;
                }
            }
            break;
        }
        else
        {
            data = 1000;
        }
    }
}

int main()
{

    map<int, string> m1;
    map<int, string> m2;
    m2[1] = "30 days";
    m2[2] = "28 or 29 days";
    m2[3] = "31 days";
    m2[4] = "30 days";
    m2[5] = "31 days";
    m2[6] = "30 days";
    m2[7] = "31 days";
    m2[8] = "31 days";
    m2[9] = "30 days";
    m2[10] = "31 days";
    m2[11] = "30 days";
    m2[12] = "31 days";

    m1[1] = "january";
    m1[2] = "february";
    m1[3] = "march";
    m1[4] = "april";
    m1[5] = "may";
    m1[6] = "june";
    m1[7] = "july";
    m1[8] = "august";
    m1[9] = "september";
    m1[10] = "october";
    m1[11] = "november";
    m1[12] = "december";
    string month;
    cout << "Input : ";
    cin >> month;
    finder(m1, m2, month);
    print_map(m1, m2);
    return 0;
}
