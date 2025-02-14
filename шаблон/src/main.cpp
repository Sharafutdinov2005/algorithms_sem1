#include <iostream>
#include <exception>

int main()
try
{
    return 0;
}
catch(std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return 1;
}
catch(...)
{
    std::cout << "Something went wrong... :(" << std::endl;
}