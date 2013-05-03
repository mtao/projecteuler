
fn triangleNum(x: int) -> int {
    return x*(x+1) / 2;
}

fn sumOfProducts(x: int, max: int) -> int {
    let nums: int = max/x as int;
    return triangleNum(nums) * x;
}

fn sumOfTwoProducts(x: int, y: int, max: int) -> int {

    let sop = sumOfProducts;
    let mmax = max-1;
    return sop(x,mmax) + sop(y,mmax) - sop(x*y,mmax);

}

fn main() {
    let sotp = sumOfTwoProducts;
    io::println(fmt!("%d",sotp(3,5,1000)));
    
}
