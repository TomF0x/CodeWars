package main

// CodeWars Highest Scoring Word (Kyu 6) https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/go
// Done in Base go (No import)

func High(s string) string {
	var mylist = append([]string{})
	var tempword string
	for _, letter := range s {
		if string(letter) == " " {
			mylist = append(mylist, tempword)
			tempword = ""
		} else {
			tempword += string(letter)
		}
	}
	mylist = append(mylist, tempword)
	var listscoreword = append([]int32{})
	for _, word := range mylist {
		var scoreword int32 = 0
		for _, letter := range word {
			scoreword += letter - 96
		}
		listscoreword = append(listscoreword, scoreword)
		scoreword = 0
	}
	var maxscore int32 = 0
	var indexmaxscore int32 = 0
	for loop, score := range listscoreword {
		if score > maxscore {
			maxscore = score
			indexmaxscore = int32(loop)
		}
	}
	return mylist[indexmaxscore]
}

func main() {
	print(High("man i need a taxi up to ubud"))
}
