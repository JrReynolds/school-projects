//
// Created by jason on 10/4/16.
//

#ifndef JULIA_COLORS_JCOLORS_H
#define JULIA_COLORS_JCOLORS_H

#include <string>
#include <vector>
#include <array>

class JColors {
    public:
        JColors(std::string infile, std::string outfile);
        int Colorify(int val);
        std::vector<std::array<int, 3>> GenerateColors(int max);
        ~JColors();

    private:
        int mRED[3] = {255, 0, 0};
        int mGREEN[3] = {0, 255, 0};
        int mBLUE[3] = {0, 0, 255};

};


#endif //JULIA_COLORS_JCOLORS_H
