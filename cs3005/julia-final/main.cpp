#include <iostream>
#include "JEscape.h"
#include <string>

int main() {
//    int width = 20;
//    int height = 20;
//    double ac = 0.271;
//    double bc = 0.314;
//    int iterations = 12;

    int width;
    int height;
    double ac;
    double bc;
    int iterations;
    std::string output;

    std::cout << "enter width: ";
    std::cin >> width;
    std::cout << std::endl << "enter height: ";
    std::cin >> height;
    std::cout << std::endl << "enter A value: ";
    std::cin >> ac;
    std::cout << std::endl << "enter B value: ";
    std::cin >> bc;
    std::cout << std::endl << "enter max iterations: ";
    std::cin >> iterations;
    std::cout << std::endl << "enter output file name: ";
    std::cin >> output;

    JEscape juliaset(width, height, ac, bc, iterations, output);

    return 0;
}