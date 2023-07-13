/*
Пользователь вводит N и M –количество строк и столбцов в матрице. 
Программа должна заполнить матрицу случайными двузначными числами и  корректно вывести полученную матрицу в консоль. 
После этого пользователь вводит номер строки или столбца, а программа выводит сумму чисел в соответствующей строке или соответствующем столбце
*/

#include <iostream>

using namespace std;

int print_matrix_sum(int matrix[100][100], int size_rows, int size_cols, int r, string ans)
{   
    int sum = 0;
    if(ans == "row")
    {
        for(int j = 0; j < size_cols; ++j)
        {
            sum += matrix[r][j];
        }
    }
    else
    {
        for(int i = 0; i < size_rows; ++i)
        {
            sum += matrix[i][r];
        }
    }
    return sum;
}

int main()
{
    int n, m;
    cout << "Enter size rows: ";
    cin >> n;
    cout << "Enter size columns: ";
    cin >> m;

    int rand_matrix[100][100];
    
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            rand_matrix[i][j] = rand() % 199 - 99;
        }
    }

     for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < m; ++j)
        {
            cout << rand_matrix[i][j] << " ";
        }
        cout << endl;
    }

    int row, col;
    string rc;
    cout << "Enter \"row\" or \"col\": ";
    cin >> rc;
    if(rc == "row")
    {
        cout << "Enter num row: ";
        cin >> row;
        cout << "Row " << row << " sum: " << print_matrix_sum(rand_matrix, n, m, row, rc) << endl;
    }
    else
    {
        cout << "Enter num column: ";
        cin >> col;
        cout << "Column " << col << " sum: " << print_matrix_sum(rand_matrix, n, m, col, rc) << endl;
    }
}