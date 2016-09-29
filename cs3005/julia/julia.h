#ifndef JULIA_H
#define JULIA_H

#include <string>


class Julia{
    public:
        Julia(unsigned int width, unsigned int height, unsigned int repetitions, double a, double b, char outfile[]);
        ~Julia();
        void GenerateGrid();
        void ProcessGrid();
        int ProcessCoords(double x, double y);
        double distance(double x1, double y1, double x2, double y2);

    private:
        int mWidth;
        int mHeight;
        int mReps;
        double mAConst;
        double mBConst;
        std::string mOutfile;


};

#endif //JULIA_H