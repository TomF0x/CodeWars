package main

func SquareSum(numbers []int) int {
	var rep int
	for _, number := range numbers {
		rep += number * number
	}
	return rep
}

func main() {
	println(SquareSum([]int{1, 2}))
}
