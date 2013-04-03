object P3 extends App {


    var primes = List(BigInt(2))
    def findPrimes(x: BigInt, max: BigInt): BigInt = 
            if (primes.map(p => (x%p == 0)).reduceLeft(_||_))
                findPrimes(x+1,max)
            else
            {
                primes = x :: primes;
                if(max%x==0)
                    x
                else
                    findPrimes(x+1,max)
            }

                
    def primeFactor(x: BigInt): BigInt = {
        val divisiblePrimes = primes.filter(p => x%p == 0);

        if ( divisiblePrimes == Nil )
        {
            findPrimes(primes.head+1, x);//Take the largest value
        }
            else 
                divisiblePrimes.last//Want the smallest
    }

    def largestPrimeFactor(x: BigInt): BigInt = {
        val p = primeFactor(x)
        if(x == p) x
            else
        largestPrimeFactor(x/primeFactor(x))
    }


    override def main(args: Array[String]) {
        primes = List(BigInt(2))
        println(largestPrimeFactor(BigInt("600851475143")))
    }
}
