#include <set>
#include <iostream>


class PrimeCache {
    public:
        PrimeCache(int i);
        void update(int m);
        const std::set<int>& data() const { return m_data; }
        std::set<int>::const_iterator begin() const { return m_data.begin(); }
        std::set<int>::const_iterator end() const { return m_data.end(); }
        size_t size() const { return m_data.size(); }

        bool is_prime(int n) ;
    private:
        bool is_prime_unsafe(int n) const;
        std::set<int> m_data;
        int m_max;
};


PrimeCache::PrimeCache(int num): m_max(4) {
    m_data.clear();
    m_data.insert(2);
    m_data.insert(3);
    update(num);
}

bool PrimeCache::is_prime(int n) {
    if(m_max < n) {
        update(n);
    }
    return m_data.find(n) != m_data.end();
}
bool PrimeCache::is_prime_unsafe(int n) const {
    for(auto&& p: m_data) {
        if(n%p==0) {
            return false;
        }
    }
    return true;
}
void PrimeCache::update(int num) {
    for(int i = m_max; i <= num; ++i) {
        if(is_prime_unsafe(i)) {
            m_data.insert(i);
        }
    }
    m_max = num;
}


int main(int argc, char * argv[]) {
    PrimeCache pc(1000);
    int max_n = 0;
    int maxprod = 0;

    for(int a = -999; a < 1000; ++a) {
        for(int b = -1000; b <= 1000; ++b) {

            int n = 0;
            for(;pc.is_prime(n*n+a*n+b) ; ++n) {
                
            }
            if(n > max_n) {
                max_n = n;
                maxprod = a*b;
            }

        }
    }
        std::cout << max_n << std::endl;
        std::cout << maxprod<< std::endl;
}
