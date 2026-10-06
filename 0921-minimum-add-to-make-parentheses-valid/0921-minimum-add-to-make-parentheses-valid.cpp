class Solution {
public:
    int minAddToMakeValid(string s) {
        int OpenBrackets = 0;
        int AddBrackets = 0;

        for (auto ch : s)
        {
            if (ch == '(')
                OpenBrackets++;
            else
                if (OpenBrackets > 0)
                {
                    OpenBrackets--;
                }
                else
                    AddBrackets++;
        }
        return OpenBrackets + AddBrackets;
    }
};