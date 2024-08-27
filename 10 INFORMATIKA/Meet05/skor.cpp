#include <iostream>
using namespace std;

int main(){
    long number ;
    cin >> number;
    if (number >= 90 && number <= 100){
        cout << "A\n";
    } else if (number >= 80 && number <= 90){
        cout << "B\n";
    } else if (number >= 70 && number <= 80){
        cout << "C\n";
    }else{
        cout << "D\n";
    } 
    return 0;
}