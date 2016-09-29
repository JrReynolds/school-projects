#include "julia.h"
#include "extra.h"
#include <fstream>
#include <cmath>
#include <iostream>

Julia::Julia( unsigned int width,  unsigned int height,  unsigned int repetitions,  double a,  double b,  char outfile[])
    : mWidth(width), mHeight(height), mReps(repetitions), mAConst(a), mBConst(b), mOutfile(outfile){

}

double Julia::distance(double x1, double y1, double x2, double y2){
    double retval = std::sqrt(std::pow((x2-x1), 2)+std::pow((y2-y1), 2));
    return retval;
}


int Julia::ProcessCoords(double x, double y){
    //x = x*x - y*y + a
    //y = 2*x*y + b
    std::cout << x << " " << y << std::endl;
    int escape = 0;
    double newx;
    double newy;
//    double mx = -2.0 + 10 * (4.0/9);
//    double my = 2.0 - 10 * (4.0/9);
    for(int i = 0; i < mReps; i++){
        if(distance(0, 0, x, y) < 2.0){
            newx = (x*x)-(y*y)+mAConst;
            newy = (2.0*x*y)+mBConst;
            x = newx;
            y = newy;
            escape++;
        }
    return escape;
    }

//    int escape = 0;
//    double mx = -2.0 + 10 * (4.0/9);
//    double my = 2.0 - 10 * (4.0/9);
//    for(int i = 0; i < mReps; i++){
//        double d = distance(0, 0, mx, my);
//        if(d < 2.0){
//           std::cout << escape << std::endl;
//            escape++;
//            mx = (mx * mx) - (my * my) + mAConst;
//            my = (2.0 * mx * my) + mBConst;
//        }
//    }
//    return escape;
}

void Julia::GenerateGrid(){

}

void Julia::ProcessGrid(){

}

Julia::~Julia(){
     //is this the proper way to delete ExtraFuncs?
}