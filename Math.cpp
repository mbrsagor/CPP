#include <iostream>

using namespace std;

class Math
{
public:
    int a, b, c;

    // `add_number` is function which calculation sum a & b. Then mean `add_number` is a simple user define function
    int add_number()
    {
        c = a + b;
        return c;
    };

};

// Define main fucntion.
int main()
{
    Math math_instance; // Here after instantiating the `Math` class.
    cout << "Enter value of a: ";
    cin >> math_instance.a; // cin = Mean user input `a` variable
    cout << "Enter value of b: ";
    cin >> math_instance.b; // cin = Mean user input `b` variable

    cout << "Total Result of a+b is: " << math_instance.add_number(); // Now here access the function using class instance
}
