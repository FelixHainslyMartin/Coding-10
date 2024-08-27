#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double number_one = 2.17;
    double number_two = 3.89;

    cout << "round : " << round(number_one) << " - " << round(number_two) << endl;
    cout << "floor : " << round(number_one) << " - " << round(number_two) << endl;
    cout << "ceil : " << round(number_one) << " - " << round(number_two) << endl;
    cout << "trunc : " << round(number_one) << " - " << round(number_two) << endl;
    cout << "int : " << round(number_one) << " - " << round(number_two) << endl;
    return 0;
}