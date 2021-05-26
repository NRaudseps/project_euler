#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int all_multiples(int n) {
	vector<int> multiples;

	for (int i = 0; i < n; ++i) {
		if (i % 3 == 0 || i % 5 == 0) {
			multiples.push_back(i);
		}
	}

	int sum = accumulate(multiples.begin(), multiples.end(), 0);

	return sum;
}

int main() {
	cout << all_multiples(1000) << endl;
	return 0;
}