#include <iostream>
using namespace std;

int fibonacci(int n) {
	int sum = 0;

	for (int i = 0, a = 1, b = 1; i < n; i++, b += a, a = b - a) {
		cout << a << endl;
		if (a % 2 == 0 && b < 4000000) {
			sum += a;
		}
	}

	return sum;
}

int main(int argc, char const *argv[])
{
	cout << fibonacci(25) << endl;
	return 0;
}