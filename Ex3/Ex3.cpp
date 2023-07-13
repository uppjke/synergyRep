/*
Пользователь вводит 2 целых числа, которые задают диапазон. 
Через пробел вывести в консоль все нечётные числа из этого диапазона
*/

#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cout << "Enter start: ";
    cin >> n;
    cout << "Enter end: ";
    cin >> m;

    for(int i = n; i < m + 1;  ++i)
    {
        if(i % 2)
        {
            cout << i << " "; 
        }
        
    }
}