#include<bits/stdc++.h>
using namespace std;
const int N = 250;
int bgpr[N];
vector<int>v;
void bk(int x)
{
    if(x==bgpr[x])return;
    v.push_back(bgpr[x]);
    bgpr[x];
}
int main()
{
    for(int i=2;i<N;i++)
        if(!bgpr[i])
        for(int j=i;j<N;j+=i)
            bgpr[j]=i;
    for(int i=1;i<=20;i++)cout<<i<<' '<<bgpr[i]<<endl;
    int t,x;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&x);
        v.clear();
        bk(x);
        printf("%s\n",(v.size()==4)?"YES":"NO");
    }

}
