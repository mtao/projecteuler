object P5 extends App {
	def from(n: Int): Stream[Int] = n #:: from(n + 1)
	def sieve(s: Stream[Int]): Stream[Int] = s.head #:: sieve(s.filter(_ % s.head != 0))
	def primes = sieve(from(2))


	private def findFactor(x: BigInt, ind: Int): Int = {
		if (x % primes(ind) == 0) ind
		else findFactor(x, ind+1)
	}
	def getFactor(x: BigInt): Int = if (x < 2) -1 else findFactor(x,0)
	
	def increment(list: Array[Int], index: Int): Array[Int] = {
		if(list.length < index+1)
		{
			list ++ new Array[Int](index-list.length) :+ 1
		} 
		else
		{
			list(index) = list(index) + 1;
			list
		}
	}

	def factorization(x: BigInt): Array[Int] = {
		if (x < 2) Array[Int]()
		else
		{
			val ind = getFactor(x)
			val prime = primes(ind)
			increment(factorization(x/prime),ind)
		}
	}

	def max(x: Array[Int], y: Array[Int]): Array[Int] = {
		val ord = if (x.length > y.length) (y,x) else (x,y)
		(ord._1 zip ord._2).map(a => if(a._1 > a._2) a._1 else a._2 ) ++ ord._2.slice(ord._1.length,ord._2.length)

	}

	def pow(a: BigInt, p: Int): BigInt = p match {
		case 0 => BigInt(1)
		case _ => a * pow(a,p-1)
	}
	def evalFactorization(arr: Array[Int]): BigInt = {

		(primes zip arr).map(a=>pow(BigInt(a._1),a._2)).reduceLeft(_*_)
	}

	override def main(args: Array[String]) {
		println(
			evalFactorization(Range(2,20,1).map( factorization _ compose (a=>BigInt(a))).reduceLeft((a,b) => max(a,b)))
			)
	}
}
