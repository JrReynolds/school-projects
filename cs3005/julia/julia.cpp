#include "julia.h"

Julia::Julia(unsigned int width, unsigned int height, unsigned int repetitions, double a, double b, std::string outfile)
    : mWidth(width), mHeight(height), mReps(repetitions), mAConst(a), mBConst(b), mOutfile(outfile){

    //verify values
    if(mWidth <= 0){
        while(mWidth <= 0){
            std::cout << "Invalid width parameter (must be greater than 0). Enter again: " << std::endl;
            std::cin >> mWidth;
        }
    }
    if(mHeight <= 0){
        while(mHeight <= 0){
            std::cout << "Invalid height parameter (must be greater than 0). Enter again: " << std::endl;
            std::cin >> mHeight;
        }
    }
    if(mReps <= 0){
        while(mReps <= 0){
            std::cout << "Invalid repetitions parameter (must be greater than 0). Enter again: " << std::endl;
            std::cin >> mReps;
        }
    }
    if()
}