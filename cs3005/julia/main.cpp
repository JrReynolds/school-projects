#include <iostream>
#include "julia.h"

//if I include string here does it still need to be included in julia?
int main() {
    unsigned int width = 10;
    unsigned int height = 1;
    unsigned int repetitions = 9;
    double a = 0.271;
    double b = 0.314;
    char outfile[64] = "output.txt";


    Julia julia(width, height, repetitions, a, b, outfile); //why don't I put const in front of these? (was giving syntax error)
    for(int i = 0; i < height; i++){                            //how do I initialize class objects to the heap?
        double ni = 2.0-i*(4/height-1);
        for(int j = 0; j < width; j++){
            double nj = -2.0+j*(4/width-1);
            int escapeVal = julia.ProcessCoords(nj, ni);
            std::cout << escapeVal << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}