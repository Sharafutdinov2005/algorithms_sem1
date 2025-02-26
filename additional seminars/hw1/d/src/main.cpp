#include <iostream>

long double solve(long double a, long double b, long double c, long double d) {
    b /= a;
    c /= a;
    d /= a;

    long double l, r;

    if (d < 0)
        l = 0, r = 1e4;
    else if (d > 0)
        r = 0, l = -1e4;
    else
        return 0;

    while (r - l > 1e-4) {
        long double m = (l + r) / 2;
        long double t = (m * (m * (m + b) + c) + d);

        if (t < 1e-12 && t > -1e-12)
            return m;
        if (t > 1e-12)
            r = m;
        else
            l = m;
    }
    return r;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    long double a, b, c, d;
    std::cin >> a >> b >> c >> d;
    std::cout << solve(a, b, c, d);
    return 0;
}
