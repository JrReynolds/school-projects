#ifndef JULIA_H
#define JULIA_H

#include <string>


class Julia{
    public:
        Julia(const unsigned int width, const unsigned int height, const unsigned int repetitions, const double a, const double b, const std::string outfile);
        ~Julia();
        void GenerateGrid();
        void ProcessGrid();
        int ProcessCoords(int x, int y);



};

#endif //JULIA_H