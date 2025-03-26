#include <iostream>
#include <vector>

std::vector<int> bubble_sort(std::vector<int> vec) {
    int n = vec.size();
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n - i - 1; ++j)
            if (vec[j] >= vec[j + 1]) {
                int temp = vec[j];
                vec[j] = vec[j + 1];
                vec[j + 1] = temp;
            }
    return vec;
}

int main() {
    std::vector<int> a; int n; std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int x; std::cin >> x;
        a.push_back(x);
    } std::vector<int> ans{bubble_sort(a)};
    for (int i = 0; i < n; ++i) {
        std::cout << ans[i] << " ";
    }
    return 0;
}
