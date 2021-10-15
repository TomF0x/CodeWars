package main

import "fmt"

func MultiplicationTable(size int) [][]int {
	table := make([][]int,size)
	for y:=0;y<size;y++{
		for x:=1;x<size;x++{
			table[y] = append(table[y],(y+1)*x)
		}
	}
	return table
}

func main() {
	fmt.Println(MultiplicationTable(1))
	fmt.Println(MultiplicationTable(2))
	fmt.Println(MultiplicationTable(3))
}
