//
// Created by jason on 10/4/16.
//

#ifndef JULIA_COLORS_RGB_H
#define JULIA_COLORS_RGB_H

#include <string>

class RGB {
    public:
        RGB(int r, int g, int b);
        std::string print();
        void updateAll(int r, int g, int b);
        void updateR(int r);
        void updateG(int g);
        void updateB(int b);
    private:
        int mData[3] = {0,0,0};
        int maxValue = 255;
};


#endif //JULIA_COLORS_RGB_H
