object P6 extends App {
    def sum(x: Int): Int = x * (x+1) / 2
    def sumFunc_(x: Int, end: Int): Int = if (x<=end) {
        x * (sum(end)-x) + sumFunc_(x+1,end)
    } else {
        0
    }
    def sumFunc(x: Int): Int = sumFunc_(1,x)

    override def main(args: Array[String]) {
        println(sumFunc(4))
        println(sumFunc(10))
        println(sumFunc(100))
    }
}
