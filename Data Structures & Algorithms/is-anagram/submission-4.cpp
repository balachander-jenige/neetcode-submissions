class Solution {
public:
    bool isAnagram(string s, string t) {
          if (s.size() != t.size())
            return false;
        unordered_map<char, int> ana;
        for (int i=0;i<s.size();i++){
            ana[s[i]] ++;
        }
        for (int i=0;i<t.size();i++){
            ana[t[i]] --;
            if(ana[t[i]]<0)
            {
                return false;
            }
        }
        return true;

    }
};
