package main

import "fmt"

func Solution(str string) []string {
	rep := append([]string{})
	for i:=0;i<len(str)-1;i+=2{
		rep = append(rep,string(str[i])+string(str[i+1]))
	}
	if len(str)%2==1 {
		rep = append(rep,string(str[len(str)-1])+"_")
	}
	return rep
}

func main() {
	fmt.Println(Solution("dawsd"))
}
