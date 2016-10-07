#include "JColors.h"
#include <fstream>
#include <iostream>

JColors::JColors(std::string infile, std::string outfile, int maxColor){
    std::ofstream out;
    std::ifstream in;


    std::string line;

    int width;
    int height;
    int its;

    in.open(infile);
    out.open(outfile);

    in >> width >> height >> its;
    out << width << " " << height << " " << maxColor << std::endl;

    std::vector<std::vector<int>> colors = GenerateGradient(mRED, mBLUE, its);

    while(getline(in, line)){
        int escapeVal;
        for(int i = 0; i<width; i++){
            in >> escapeVal;
            for(int j = 0; j<3;j++) {
                out << colors[escapeVal][j] << " ";
            }
        }
        out << std::endl;
    }

    in.close();
    out.close();

}

std::vector<std::vector<int>> JColors::GenerateColors(int max){
    std::vector<std::vector<int>> colors = GenerateGradient(mRED, mBLUE, max);
    for(int i = 0; i < colors.size(); i++){
        std::cout << "[";
        for(int j = 0; j < colors[i].size(); j++){
            std::cout << colors[i][j] << ", ";
        }
        std::cout << "]" << std::endl;
    }
    for(int i = 0; i < max; i++){

    }




    return colors;

}

std::vector<std::vector<int>> JColors::GenerateGradient(std::vector<int> & start, std::vector<int> & end, int step){
    //initialize return vector
    std::vector<std::vector<int>> gradientColors;
    //a final number will be added to make up for the remaining rgb values, so to get step number of colors total we must subtract one here
//    step = step-1;
    //get the amount we need to change r g and b by each iteration
    double rDiff = (start[0] - end[0])/(double)step;
    std::cout << rDiff << std::endl;
    double gDiff = (start[1] - end[1])/(double)step;
    double bDiff = (start[2] - end[2])/(double)step;
    //get the difference between the color at the end of the for loop and the desired end value
    int rRem = (rDiff * step) - (start[0] - end[0]);
    std::cout << rRem << std::endl;
    int gRem = (gDiff * step) - (start[1] - end[1]);
    int bRem = (bDiff * step) - (start[2] - end[2]);
    //get the first values and append them to the return vector
    for(int i = 0; i < step; i++) {
        int newR = start[0] - (i*rDiff);
        int newG = start[1] - (i*gDiff);
        int newB = start[2] - (i*bDiff);
        std::vector<int> gradColor = {newR, newG, newB};
        gradientColors.push_back(gradColor);
    }
    std::vector<int> finalColor = {end[0] + rRem, end[1] + gRem, end[2] + bRem};
    gradientColors.push_back(finalColor);
    return gradientColors;
}

int JColors::Colorify(int val) {
    //get the escape value
    //associate it with a color
        //establish gradients
        //create color map

}

JColors::~JColors(){

}