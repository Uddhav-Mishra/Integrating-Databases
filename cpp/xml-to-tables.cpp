#include<bits/stdc++.h>
#define ll long long int
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define ioS ios::sync_with_stdio(false);
#define re0 return 0;
using namespace std ;

map<string,ll> m ; // string to node id
map<ll,string> m1 ;  // node to string
map<string,string> m2 ; // data type for leaves

ll indeg[20000] ;
vector<ll> v[20000] ;
ll vis[20000] ;
vector<pair<string,string> > ans[2000] ;
int ia = 0 ;

void dfs(int node,string s ){ //cout << "dfs of " << m1[node] << endl ;
vis[node]=1;
if(m2[m1[node]]!=""){ans[ia].pb(mp(s,m2[m1[node]])) ;//cout << "pushed string " << s << endl ;
}
for(int i=0;i<v[node].size();i++){
    dfs(v[node][i],(s+"."+ m1[v[node][i]]));
}
}

int main(){
    ioS ;
int i ;
  ifstream file("a5.txt");
     string s; string t ; int id=1 ;
    while (std::getline(file, s))
    {
        //cout <<  s << endl ;
         t="" ;
        int src = 0 ; string prev  ; int flag1=0;
for(i=9;i<s.size();i++){
if(!(s[i]==' '||s[i]=='('||s[i]==')'||s[i]=='#'||s[i]=='>'||s[i]==',')){
    t = t + s[i] ;
}
else{
    if(t.size()>0){  //cout << t << endl ;
        if(m[t]==0){
          m[t]=id ;  m1[id++]=t;
        }
    if(flag1==0){flag1=1;src = m[t] ;}
    //if(t=="name"){cout << "prev " <<  prev << endl ;}
        if(t=="PCDATA"||t=="integer"){
            m2[prev]=t ;
        }
        else{
          if(m[t]!=src){  v[src].pb(m[t]) ; indeg[m[t]]++; //cout << "Edge btwn " << m1[src] << "  " << t << endl ;
          }
        }
         prev = t ;t="";
    }
t="" ;
}
}
}



for(int ii=1;ii<id;ii++){
    if(indeg[ii]==0&&(m1[ii]!="PCDATA"&&m1[ii]!="integer")){
      ia++; ans[ia].pb(mp(m1[ii]," ")) ; dfs(ii,m1[ii]) ;
    }
}

for(i=1;i<=ia;i++){
    for(int j=0;j<ans[i].size();j++){
        if(j==0){cout << "table name : "  << ans[i][j].ff << endl ;cout << "attributes :\n";}
       if(j>0) cout << ans[i][j].ff << ": type = " << ans[i][j].ss << endl ;
    }
    cout << endl ;
}



}
