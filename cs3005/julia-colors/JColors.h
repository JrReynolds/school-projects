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
        std::vector<std::vector<int>> GenerateColors(int max);
        std::vector<std::vector<int>> & GenerateGradient(std::vector<int> & start, std::vector<int> & end, int step);
        ~JColors();

    private:
        std::vector<int> mRED = {255, 0, 0};
        std::vector<int> mGREEN = {0, 255, 0};
        std::vector<int> mBLUE = {0, 0, 255};

};


#endif //JULIA_COLORS_JCOLORS_H
