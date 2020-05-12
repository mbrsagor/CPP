#include <iostream>

using namespace std;

class Box
{
public:
    double l;
    double h;
    double w;
};

int main()
{
    Box b1;
    Box b2;
    cout << "Enter the value l, h, w for the box:";
    cin >> b1.l;
    cin >> b1.h;
    cin >> b1.w;

    cout << "Enter the value l, h, w for the box2:" << endl;
    cin >> b2.l;
    cin >> b2.h;
    cin >> b2.w;

    cout << "Volume of box1 is: " << b1.l * b1.h * b1.w << endl;
    cout << "Volume of box2 is: " << b2.l * b2.h * b2.w << endl;
}
