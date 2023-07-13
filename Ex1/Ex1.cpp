/*
Напишите программу, которая поочерёдно запрашивает у пользователя
переменные различных типов, после чего выводит их все через пробел обратно в консоль. 
Обязательно использовать такие типы данных как int, double, char, bool, string. 
То есть, например, программа просит пользователя
“Enter int: “, затем “Enter double: “ и так далее, а в конце выводит “You entered: 5 3.14 random_string “ и так далее.
*/
#include <iostream>

using namespace std;

int main()
{
    int i;
    double d;
    char c;
    bool b;
    string s;

    cout << "Enter int: ";
    cin >> i;
    cout << "Enter double: ";
    cin >> d;
    cout << "Enter char: ";
    cin >> c;
    cout << "Enter bool: ";
    cin >> b;
    cout << "Enter string: ";
    cin >> s;

    cout << endl << "You entered: " << i << " " << d << " " << c << " " << b << " " << s << endl;

}