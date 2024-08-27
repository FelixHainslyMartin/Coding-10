#include <iostream>
#include <cmath>
using namespace std;

double find_area(double a, double t){
    double result;
    result = a * t / 2;
    return result;
}

double find_perimeter(double a, double t){
    double result;
    double s;
    s = sqrt(pow(a,2) + pow(t,2));
    result = a + t + s;
    return result;
}

int main (){
    int alas, tinggi;
    cin >> alas >> tinggi;
    cout << "area : " << find_area(alas, tinggi) << endl;
    cout << "perimeter : " << find_perimeter(alas, tinggi) << endl;
    return 0;
}