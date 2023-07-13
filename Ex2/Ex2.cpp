/*
Пользователь вводит 2 целых числа, программа должна вывесит “YES”, 
если хотя бы одно из чисел чётное, или “NO”, если все числа нечётные.
*/

#include <iostream>

using namespace std;


int main()
{
    int n1, n2;

    cout << "Enter number 1: ";
    cin >> n1;
    cout << "Enter number 2: ";
    cin >> n2;

    if(n1 % 2 && n2 % 2)
    {
        cout << "NO";
    }
    else
    {
        cout << "YES";
    }
}