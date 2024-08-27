#include <iostream>
using namespace std;

int main() {
    int totalSteps;
    cout << "Jumlah tangga : ";
    cin >> totalSteps;

    for (int i = 0; i <= totalSteps; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "#";
        }
        cout << "\n";
    }
    return 0;
}