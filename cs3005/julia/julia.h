#ifndef JULIA_H
#define JULIA_H

#include <string>
#include <fstream>

class Julia{

    Julia::Julia(unsigned int width, unsigned int height, unsigned int repetitions, double a, double b, std::string outfile);
    Julia::GenerateGrid();
    Julia::ProcessGrid();

};

#endif //JULIA_H