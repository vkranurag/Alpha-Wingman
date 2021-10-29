#include<iostream>
#include<stack>
using namespace std;

stack<int> sortStack(stack<int> &input)
{
    stack<int> tempStack;
 
    while (!input.empty())
    {
        int temp = input.top();
        input.pop();
        while (!tempStack.empty() && tempStack.top() < temp)
        {
            input.push(tempStack.top());
            tempStack.pop();
        }
        tempStack.push(temp);
    }
 
    return tempStack;
}
int main()
{
    stack<int> input;
    input.push(34);
    input.push(3);
    input.push(31);
    input.push(98);
    input.push(92);
    input.push(23);
    stack<int> tempStack = sortStack(input);
    cout << "Sorted numbers are:\n";
    while (!tempStack.empty())
    {
        cout << tempStack.top()<< " ";
        tempStack.pop();
    }

}