#include <iostream>
#include <array>
#include <vector>

template <typename T>
auto sortVector(std::vector<T> array, bool ascending) -> std::vector<T> {
    std::vector<T> sortedArray{};
    for (size_t i{ 0 }; i < array.size(); ++i) sortedArray.push_back(array[i]);

    for (size_t i{ 0 }; i < sortedArray.size(); ++i) {
        for (size_t j{ 0 }; j < sortedArray.size(); ++j) {        
            if (ascending ? (sortedArray[j] > sortedArray[i]) : (sortedArray[j] < sortedArray[i]))
                std::swap(sortedArray[i], sortedArray[j]);
        }
    }

    return sortedArray;
}

auto main() -> int {
    std::vector<double> stuff{ 20004, 1, 3, 5, 10, 2, 123, -45, 4.345, 45.6, 24, 2, -4, 2, 2, 2, 4, 5, -2, 1 };
    std::vector<double> sortedStuff{ sortVector(stuff, true) };
    for (size_t i{ 0 }; i < sortedStuff.size(); ++i) 
        std::cout << sortedStuff[i] << (i != sortedStuff.size() - 1 ? ", " : "\n");

    return 0;
}