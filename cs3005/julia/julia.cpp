#include "julia.h"
#include "extra.h"
#include <fstream>

Julia::Julia(const unsigned int width, const unsigned int height, const unsigned int repetitions, const double a, const double b, const std::string outfile)
    : mWidth(width), mHeight(height), mReps(repetitions), mAConst(a), mBConst(b), mOutfile(outfile){

    extra ExtraFuncs();
    //extra *ExtraFuncs = new extra(); is this the proper way to allocate data to the heap?
    //verify values
//    if(mWidth <= 0){
//        while(mWidth <= 0){
//            std::cout << "Invalid width parameter (must be greater than 0). Enter again: " << std::endl;
//            std::cin >> mWidth;
//        }
//    }
//    if(mHeight <= 0){
//        while(mHeight <= 0){
//            std::cout << "Invalid height parameter (must be greater than 0). Enter again: " << std::endl;
//            std::cin >> mHeight;
//        }
//    }
//    if(mReps <= 0){
//        while(mReps <= 0){
//            std::cout << "Invalid repetitions parameter (must be greater than 0). Enter again: " << std::endl;
//            std::cin >> mReps;
//        }
//    }
//    if()

}

int Julia::ProcessCoords(int x, int y){
    //x = x*x - y*y + a
    //y = 2*x*y + b
    int escape = 0;
    for(int i = 0; i < mReps; i++) {
        double x = (x * x) - (y * y) + mAConst;
        double y = (2 * x * y) + mBConst;
        double distance = ExtraFuncs.distance(0, 0, x, y);
        if(!distance >= 2){
            escape++;
        }
    }
    return escape;
}

void Julia::GenerateGrid(){

}

void Julia::ProcessGrid(){

}

Julia::~Julia(){
    delete ExtraFuncs; //is this the proper way to delete ExtraFuncs?
}