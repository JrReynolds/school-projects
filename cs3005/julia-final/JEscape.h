#ifndef JULIAESCAPE_JESCAPE_H
#define JULIAESCAPE_JESCAPE_H

#include <string>

class JEscape {
    public:
        JEscape(int width, int height, double a, double b, int iterations, std::string output);
        double distance(double x1, double x2, double y1, double y2);
        int ProcessCoords(double x, double y);
    private:
        int mWidth;
        int mHeight;
        double mA;
        double mB;
        int mReps;
        std::string mOutput;
};


#endif //JULIAESCAPE_JESCAPE_H
