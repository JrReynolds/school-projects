#include <iostream>
#include <cmath>
#include <fstream>

double distance(double x1, double y1, double x2, double y2){
    double retval = std::sqrt((std::pow((x2-x1), 2)+std::pow((y2-y1), 2)));
    return retval;
}

int processCoords(double x, double y, int reps){
    double newx = x;
    double newy = y;
    int escape = 0;
    for(int i = 0; i < reps; i++){
        if(distance(0, 0, newx, newy) >= 2.0){
            return escape;
        }
        double newxH = (newx*newx) - (newy*newy) + 0.271;
        double newyH = (2*newx*newy) + 0.314;
        newx = newxH;
        newy = newyH;
        escape++;
    }
    return escape;
//    std::cout << "(" << newx << ", " << newy << ")" << std::endl;
}

int main() {
//    int width = 20;
//    int height = 20;
//    double ac = 0.271;
//    double bc = 0.314;
//    int iterations = 12;

    int width;
    int height;
    double ac;
    double bc;
    int iterations;

    std::ofstream fileObject;

    fileObject.open("./output.txt", std::ios::app);

    std::cout << "enter width: ";
    std::cin >> width;
    std::cout << std::endl << "enter height: ";
    std::cin >> height;
    std::cout << std::endl << "enter A value: ";
    std::cin >> ac;
    std::cout << std::endl << "enter B value: ";
    std::cin >> bc;
    std::cout << std::endl << "enter max iterations: ";
    std::cin >> iterations;

    int escapeValue;

    for(int i = 0; i < height; i++){
        double paramI = 2.0-(i*(4.0/(height-1)));
        for(int j = 0; j < width; j++){
            double paramJ = -2.0+(j*(4.0/(width-1)));
//            std::cout << "(" << paramJ << " " << paramI << ")";
            escapeValue = processCoords(paramJ, paramI, iterations);
            fileObject << escapeValue << " ";
        }
        fileObject << std::endl;
    }
    fileObject.close();
    return 0;
}