//
// Created by jason on 10/4/16.
//

#include <sstream>
#include "RGB.h"

RGB::RGB(int r, int g, int b){
    updateAll(r, g, b);
}

void RGB::updateAll(int r, int g, int b) {
    updateR(r);
    updateG(g);
    updateB(b);
}

void RGB::updateR(int r){
    if(r > maxValue){
        mData[0] = maxValue;
    }
    else if(r < 0){
        mData[0] = maxValue;
    }
    else{
        mData[0] = r;
    }
}

void RGB::updateG(int g){
    if(g > maxValue){
        mData[1] = maxValue;
    }
    else if(g < 0){
        mData[1] = maxValue;
    }
    else{
        mData[1] = g;
    }
}

void RGB::updateB(int b){
    if(b > maxValue){
        mData[2] = maxValue;
    }
    else if(b < 0){
        mData[2] = maxValue;
    }
    else{
        mData[2] = b;
    }
}

std::string RGB::print(){
    std::string retval = "";
    std::stringstream converter;
    converter << mData[0] << " " << mData[1] << " " << mData[2];
    retval = converter.str();
    return retval;
}