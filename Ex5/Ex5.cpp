/*
Напишите рекурсивную функцию, которая переводит число из десятичной системы в двоичную. 
Допускается использовать тип string для хранения двоичного числа.
*/

#include <iostream>

using namespace std;

string bn = "";

int bin(int n)
{
    bn += to_string(n % 2);
    if(n == 0) return 0;
    else if(n == 1) return 1;
    return bin(n / 2);
}

int main()
{
    // 44 - 101100
    int n;
    cout << "Enter 10 base num: ";
    cin >> n;
    bin(n);
    for(size_t i = 0; i < bn.size() / 2; ++i)
    {
        swap(bn[i], bn[bn.size() - i - 1]);
    }
    cout << "Bin num: " << bn << endl;
}