#include "JColors.h"
#include <fstream>
#include <iostream>

JColors::JColors(std::string infile, std::string outfile)
        :
{
    std::ofstream out;
    std::ifstream in;

    std::string line;

    in.open(infile);
    out.open(outfile);



    in.close();
    out.close();

}

std::vector<std::array<int, 3>> generateColors(int max){

}

int JColors::Colorify(int val) {
    //get the escape value
    //associate it with a color
        //establish gradients
        //create color map

}

JColors::~JColors(){

}