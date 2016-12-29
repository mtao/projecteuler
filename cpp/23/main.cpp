#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
std::set<int> ab;
std::map<int,int> fsum;
std::vector<int> primes;


int get_fsum(int num) {
    int sum = 0;
    for(int i = 1 ; i < num; ++i) {
        if(num%i == 0) {
            sum += i;
        }
    }
    return sum;

}


int main() {
	long long sum = 0;
    primes.push_back(2);
    int count = 28123;
	for(int i = 1; i < count; ++i) {
        fsum[i] = get_fsum(i);
        if(fsum[i] > i) {
            ab.insert(i);
        }
    }
    for(int i = 1; i < count; ++i) {
        for(auto&& a: ab) {
            int desired = i - a;
            if(desired < 0) {
                break;
            }
            if(ab.find(desired) != ab.end()) {
                goto endloop;
            }
        }
        sum += i;
        std::cout << i << std::endl;
endloop:
        continue;
    }
    std::cout << sum << std::endl;

	return 0;
}
