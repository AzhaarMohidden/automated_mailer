#include <iostream>
#include "stdlib.h"

using namespace std;

int main(){

  int var = 8;
  int* ptr2 = new int;
  int* ptr = &var;
  cout<< *ptr <<" " << *ptr2 << endl;
  *ptr2 = 5;
  cout<< *ptr <<" " << *ptr2 << endl;
  *ptr2 = 7;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  *ptr2 = 4;
  delete ptr2;

  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;
  ptr2 = new int(10);
  cout<< *ptr <<" " << *ptr2 << endl;
  cout<< *ptr <<" " << *ptr2 << endl;


}
