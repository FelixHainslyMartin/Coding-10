#include <iostream>
using namespace std;

int main(){
    // vertical -> ####
    int bricks;
    cout << "Input number of brick : ";
    cin >> bricks;
    for (int i = 0; i < bricks; i++){
        cout << "#" << endl;
    } cout << endl;

    return 0;
}