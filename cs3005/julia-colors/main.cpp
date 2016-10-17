#include <iostream>
#include "JColors.h"

int main(){
    //create new colors object
    //use object to convert escape values to colors
        //load escape values
        //read escape values
        //convert escape values
    std::string in;
    std::string out;
    int MaxColor;

    std::cout << "Enter max color: " << std::endl;
    std::cin >> MaxColor;
    std::cout << "Enter input file: " << std::endl;
    std::cin >> in;
    std::cout << "Enter output file: " << std::endl;
    std::cin >> out;

    JColors julia(in, out, MaxColor);
    return 0;
}