#include <iostream>
using namespace std;

int main() {
  int a,b,c;
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin>>a;

  for(int i=0;i<a;i++){
    cin>>b>>c;
    cout<<b+c;
    cout<<"\n";
  }
 
} 