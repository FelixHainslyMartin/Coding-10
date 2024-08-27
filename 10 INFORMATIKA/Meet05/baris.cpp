#include <iostream>
using namespace std;

int main(){
    // 4, 14, 24, 34 ...(< 100)
    //looping while
    int i = 4;
    while (i < 100){
        cout << i << " ";
        i += 10;       
    }
    cout << endl;
    for (int i = 101; i > 0; i-=5){
        cout << i << " ";
    }
    cout << endl;
    for (int i = 2; i<= 1000; i*=2){
        cout << i << " ";
    }
    cout << endl;
    for (int i = 80; i>= 5; i/=2){
        cout << i << " ";
    }
    return 0;
}