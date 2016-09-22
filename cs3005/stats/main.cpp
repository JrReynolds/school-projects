#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

void printVector(const std::vector<float> & vec){
    for(int i = 0; i < vec.size(); i++){
        std::cout << vec.at(i) << " ";
    }
    std::cout<<std::endl;
    return;
}

int main(){

    float Sum = 0;
    float current;
    float counter = 0;
    float maximum;
    float minimum;
    bool firstLoop = true;
    std::vector<float> numbers;

    std::cout << "Enter numbers to calculate. When finished, enter EOF command (Linux ctrl-d, windows ctrl-z)." << std::endl;

    while(std::cin >> current){
        Sum += current;
        counter++;
        numbers.push_back(current);
        if(firstLoop){
            maximum = current;
            minimum = current;
            firstLoop = false;
        }
        else{
            if(current > maximum){
                maximum = current;
            }
            if(current < minimum){
                minimum = current;
            }
        }

    }

    std::sort(numbers.begin(), numbers.end());
    int middle = numbers.size()/2;
    float median = 0;
    if(numbers.size() % 2 == 0){
        float num1 = numbers.at(middle-1);
        float num2 = numbers.at(middle);
        median = (num1+num2)/2;

    }
    else{
        median = numbers.at(middle);
    }
    printVector(numbers);
    std::cout << "Sum is: " << Sum << std::endl;
    std::cout << "Count is: " << counter << std::endl;
    std::cout << "Average is: " << Sum/counter << std::endl;
    std::cout << "Minimum is: " << minimum << std::endl;
    std::cout << "Maximum is: " << maximum << std::endl;
    std::cout << "Median is: " << median << std::endl;

    return 0;
}

