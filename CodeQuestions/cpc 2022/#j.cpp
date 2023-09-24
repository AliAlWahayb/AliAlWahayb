#j
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int S;
cin>>S;
for(int i=0;i<to_string(S).length();i++){
    if count(S.begin(),S.end(),S[i])>1{
        auto pos = S.find(S[i]);
        if (pos != std::string::npos)    
            S.erase(pos);

    }

}
cout<<S;
return 0;