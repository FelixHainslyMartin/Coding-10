#include <iostream>
using namespace std;

int main(){
    string cars[5] = {"BMW", "Porsche", "Bugatti" , "Lamborghini", "Ferrari"};
    for (string car : cars)
        cout << car << endl;
    return 0;
}