#include <iostream>
using namespace std;

int main() {
    int age;
    string name;
    cout <<"What is your name? ";
    // cin >> name;
    getline(cin, name);
    cout <<"Hi " << name << endl;
    cout << "How old are you ? ";
    cin >> age;

    if (age < 30){
    cout << "Your need to get older masbro " << age << endl;
    } else {
    cout << "Your so old masbro " << age << endl;
    }

    return 0;
}