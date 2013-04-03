object P2 extends App {
    def sumEvenFib(n_2: Int, n_1: Int, max: Int): Int = {
        val n = n_2 + n_1;
        if(n >= max) 0 else {
            if (n % 2 ==0) 
                n + sumEvenFib(n_1, n, max)
            else
                sumEvenFib(n_1, n, max)
        }

    }
    override def main(args: Array[String]) {
        println(sumEvenFib(1,1,4000000))

    }
}
