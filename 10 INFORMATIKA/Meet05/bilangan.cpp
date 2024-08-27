#include <iostream>
using namespace std;

int main(){
    long long x;
    cin >> x;
    if (x > 0){
        cout << "x is positive\n";
    } else if (x < 0){
        cout << "x is negative\n";
    }else if (x == 0){
        cout << "x is zero\n";
    }
    return 0;
}