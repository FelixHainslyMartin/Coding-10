#include <iostream>
using namespace std;

int main(){
    int x;
    cout << "The dimension : ";
    cin >> x;
    // for (int i = 1; i <= x; i++){
    //     for (int j = 0; j < 1; j++){
        for (int i = 0; i < x; i++){
            for (int k = 1; k < x-i; k++){
                cout << " ";
        }
            for (int j = 0; j <= i; j++){
                cout << "#";
        }
        cout << endl;
    }
    return 0;
}