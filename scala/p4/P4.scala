object P4 extends App {
    override def main(args: Array[String]) {
        def isPalendrome(x: Int): Boolean = ((str:String) => str == str.reverse)(x.toString)
        println(((for (num <- Range(100,1000,1)) yield for (num2 <- Range(num,1000,1)) yield num*num2).flatten.filter(isPalendrome)).max)
            
    }
}
