#include <iostream>
#include <array>
#include <vector>
#include <type_traits>

template <typename T>
auto sortVector(std::vector<T> array, bool ascending) -> std::vector<T> {
    std::vector<T> sortedArray{};
    for (size_t i{ 0 }; i < array.size(); ++i) sortedArray.push_back(array[i]);

    constexpr bool isNestedVector{ requires{ sortedArray[0].length(); sortedArray[0].size(); } };

    for (size_t i{ 0 }; i < sortedArray.size(); ++i) {
        for (size_t j{ 0 }; j < sortedArray.size(); ++j) {
            if constexpr (!isNestedVector) {
                if (ascending ? (sortedArray[j] > sortedArray[i]) : (sortedArray[j] < sortedArray[i]))
                    std::swap(sortedArray[i], sortedArray[j]);
            }
            else {
                if (ascending ? (sortedArray[j].length() > sortedArray[i].length()) : (sortedArray[j].length() < sortedArray[i].length()))
                    std::swap(sortedArray[i], sortedArray[j]);
            }
        }
    }

    return sortedArray;
}

auto main() -> int {
    auto printVector{ 
        []<typename T>(std::vector<T>& vec) -> void {
            for (size_t i{ 0 }; i < vec.size(); ++i) 
                std::cout << vec[i] << (i != vec.size() - 1 ? ", " : "\n");
        } 
    };

    std::vector<float> stuff{ 20004, 1, 3, 5, 10, 2, 123, -45, 4.345, 45.6, 24, 2, -4, 2, 2, 2, 4, 5, -2, 1 };
    std::vector<float> sortedStuff{ sortVector(stuff, true) };
    printVector(sortedStuff);

    std::vector<std::string> stringStuff{ "jim", "bob", "vim", "linus", "jeffery", "Maxmillian Robespierre", "no" };
    std::vector<std::string> sortedStringStuff{ sortVector(stringStuff, true) };
    printVector(sortedStringStuff);
    
    return 0;
}