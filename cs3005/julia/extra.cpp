#include "extra.h"
#include <cmath>


extra::extra(){}

double extra::distance(double x1, double y1, double x2, double y2){
    double retval = std::sqrt(std::pow((x2-x1), 2)+std::pow((y2-y1), 2));
    return retval;
}