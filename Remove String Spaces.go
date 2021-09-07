package main

func NoSpace(word string) string {
	var rep string
	for _, letter := range word {
		if letter != 32 {
			rep += string(letter)
		}
	}
	return rep
}

func main() {
	println(NoSpace("8 j 8   mBliB8g  imjB8B8  jl  B"))
}
