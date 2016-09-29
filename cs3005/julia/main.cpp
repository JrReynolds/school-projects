#include <iostream>
#include "julia.h"

//if I include string here does it still need to be included in julia?
int main() {
    unsigned int width = 0;
    unsigned int height = 0;
    unsigned int repetitions = 9;
    double a = 0.271;
    double b = 0.314;
    char outfile[64] = "output.txt";


    Julia julia(width, height, repetitions, a, b, outfile); //why don't I put const in front of these? (was giving syntax error)
    for(int i = 0; i < 10; i++){                            //how do I initialize class objects to the heap?
        for(int j = 0; j < 10; j++){
            double ni = 2.0+j*(4/10-1);
            double nj = -2.0-j*(4/10-1);
            int escapeVal = julia.ProcessCoords(nj, ni);
            std::cout << escapeVal << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}