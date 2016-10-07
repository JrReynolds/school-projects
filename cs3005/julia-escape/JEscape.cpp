#include "JEscape.h"
#include <cmath>
#include <fstream>

JEscape::JEscape(int width, int height, double a, double b, int iterations, std::string output)
    : mWidth(width), mHeight(height), mA(a), mB(b), mReps(iterations), mOutput(output){

    std::ofstream fileObject;

    fileObject.open(mOutput, std::ios::out);

    int escapeValue;
    fileObject << width << " " << height << " " << iterations << std::endl;
    for(int i = 0; i < mHeight; i++){
        double paramI = 2.0-(i*(4.0/(mHeight-1)));
        for(int j = 0; j < mWidth; j++){
            double paramJ = -2.0+(j*(4.0/(mWidth-1)));
            escapeValue = ProcessCoords(paramJ, paramI);
            fileObject << escapeValue << " ";
        }
        fileObject << std::endl;
    }
    fileObject.close();

}

int JEscape::ProcessCoords(double x, double y){
    double newx = x;
    double newy = y;
    int escape = 0;
    for(int i = 0; i < mReps; i++){
        if(distance(0, 0, newx, newy) >= 2.0){
            return escape;
        }
        double newxH = (newx*newx) - (newy*newy) + .271;
        double newyH = (2*newx*newy) + 0.314;
        newx = newxH;
        newy = newyH;
        escape++;
    }
    return escape;
}

double JEscape::distance(double x1, double y1, double x2, double y2){
    double retval = std::sqrt((std::pow((x2-x1), 2)+std::pow((y2-y1), 2)));
    return retval;
}