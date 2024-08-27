#include <iostream>

struct  Person
{
    std::string name;
    float weight;
    float height;
    int age = 15;
    bool is_married = false;

    Person(std::string n, float w, float h) : name(n), weight (w), height(h) {};
};


int main(){
{
    Person person("Jonathan Alvino", 70, 175);
    Person felix("felix", 55.5, 165.4);
    Person jayden("jayden", 65, 168);
    std::cout << felix.name << std::endl;
    std::cout << jayden.name << std::endl;
    return 0;
}

}