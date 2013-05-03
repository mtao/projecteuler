object P1 extends App{
    def triangleNum(x: Int): Int = {
        x*(x+1)/2
    }
    def numOccurences(x: Int, max: Int): Int = {
        (max/x).toInt
    }
    def sumOfMultiples(x: Int, max: Int): Int =  {
        x * triangleNum(numOccurences(x,max))
    }
    def sumOfMultiplesTwo(x: Int, y: Int, max: Int): Int =  {
        sumOfMultiples(x,max-1) + sumOfMultiples(y,max-1) - sumOfMultiples(x*y, max-1)
    }
    override def main(args: Array[String]) {
        println(sumOfMultiplesTwo(3,5,1000))
    }
}

