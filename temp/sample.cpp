// #include <iostream>
// #include "stdlib.h"
// //#include <cstdio>
//
// using namespace std;
//
// int main(){
//   for(int i = 0; i < 100000; i++){
//     //cout << i << endl;
//     printf("%d \n", i);
//   }
//   return 0;
// }
#include <iostream>
#include "stdlib.h"
//#include "opencv2/objdetect.hpp"

using namespace std;
long long int v = 0;
int main()
{
  for(int i=0; i<100000;i++)
  {
    // printf("v: %d ", v);
    // printf("i: %d \n", i);
    v = v+i;
    // cout << v << endl;
  }
  cout << v << endl;
  return 0;

}
