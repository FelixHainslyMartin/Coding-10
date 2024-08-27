#include <bits/stdc++.h>
using namespace std;

int main(){
    int money, price;
    cout << "Berapa banyak uang yang kamu miliki ? ";
    cin >> money;
    cout << "Harga satu indomie saat ini berapa ? ";
    cin >> price;
    cout << "Kamu akan memperoleh mie sebanyak : " << money / price << endl;
    cout << "Uang Kembaliannya adalah : " << money % price << endl;
    return 0;
}