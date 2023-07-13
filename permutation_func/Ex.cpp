#include <iostream>

using namespace std;

void perm(string s, bool p[], string s_cur = "", int s_len = 0)
{
    if(s_len == s.size())
    {
        cout << s_cur << endl;
        return;
    }

    for(int i = 0; i < s.size(); ++i)
    {
        if(p[i] == 0)
        {
            p[i] = 1;
            perm(s, p, s_cur + s[i], s_len + 1);
            p[i] = 0;
        }
    }
}

int main()
{
    string s = "abcde";
    bool p[s.size()];

    for(int i = 0; i < s.size(); ++i)
    {
        p[i] = 0;
    }

    perm(s, p);

    return 0;
}