package main

func alphanumeric(str string) bool {
	rep := false
	for _,letter := range str{
		if letter >= 48 && letter <= 57 || letter >= 65 && letter <= 90 || letter >= 97 && letter <= 122 {
			rep = true
		}else {
			rep = false
		}
	}
	return rep
}

func main() {
	alphanumeric("Mazinkaiser")
}
