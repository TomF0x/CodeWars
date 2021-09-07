package main

func SumCubes(n int) int {
	var rep int
	for i := 1; i <= n; i++ {
		rep += i * i * i
	}
	return rep
}

func main() {
	print(SumCubes(2))
}
