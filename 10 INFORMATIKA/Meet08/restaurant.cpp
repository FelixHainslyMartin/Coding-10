#include <iostream>

struct Restaurant
{
    std::string name;
    std::string type;

    Restaurant(std::string n, std::string t) : name(n), type(t) {}

    void describe_restaurant_1() {
        std::cout << "Nama restoran ini adalah " << this->name << std::endl;
    }

    void describe_restaurant_2() {
        std::cout << "restoran ini menyediakan masakan " << this->type << std::endl;
    }

    void open_restaurant() {
        std::cout << "restoran ini sedang buka" << std::endl;
    }
};

int main(){
    Restaurant restoran("Ispan", "Sumatera");
    restoran.describe_restaurant_1();
    restoran.describe_restaurant_2();
    restoran.open_restaurant();
    return 0;
}