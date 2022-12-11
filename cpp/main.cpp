#include <iostream>
#include <array>
#include <vector>

enum sortOrder {
    ASCENDING,
    DESCENDING
};

template <typename T>
auto sortVector(std::vector<T>& array, sortOrder order) -> std::vector<T> {
    std::vector<T> sortedArray{};
    for (size_t i{ 0 }; i < array.size(); ++i) 
        sortedArray.push_back(array[i]);

    for (size_t i{ 0 }; i < sortedArray.size(); ++i) {
        for (size_t j{ 0 }; j < sortedArray.size(); ++j) {        
            if (order == ASCENDING ? (sortedArray[j] > sortedArray[i]) : (sortedArray[j] < sortedArray[i]))
                std::swap(sortedArray[i], sortedArray[j]);
        }
    }

    return sortedArray;
}

template <typename T>
auto printVector(std::vector<T>& vec) -> void {
    for (size_t i{ 0 }; i < vec.size(); ++i) 
        std::cout << vec[i] << (i != vec.size() - 1 ? ", " : "\n");
}

auto main() -> int {
    std::vector<double> stuff{ 20004, 1, 3, 5, 10, 2, 123, -45, 4.345, 45.6, 24, 2, -4, 2, 2, 2, 4, 5, -2, 1 };
    std::vector<double> sortedStuff{ sortVector(stuff, ASCENDING) };
    printVector(sortedStuff);

    std::vector<int> stuff2{ 999, 4, 3, 3, 2, 5, 67, 78, 45, 323, -345, -6, -98, -102445533, 434339 };
    std::vector<int> sortedStuff2{ sortVector(stuff2, DESCENDING) };
    printVector(sortedStuff2);
    return 0;
}