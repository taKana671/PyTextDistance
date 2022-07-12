package main

import "C"
import "math"

//export Hamming
func Hamming(s1 string, s2 string) int {
	count := 0
	rs1 := []rune(s1)
	rs2 := []rune(s2)

	if len(rs1) != len(rs2) {
		return -1
	}

	for i := 0; i < len(rs1); i++ {
		if rs1[i] != rs2[i] {
			count += 1
		}
	}
	return count
}

// export Levenshtein
func Levenshtein(s1 string, s2 string) int {

	rs1 := []rune(s1)
	rs2 := []rune(s2)

	rs1Len := len(rs1)
	rs2Len := len(rs2)

	arr := make([][]int, rs1Len+1)

	for i := range arr {
		sub := make([]int, rs2Len+1)
		if i == 0 {
			for j := range sub {
				sub[j] = j
			}
		} else {
			sub[0] = i
		}
		arr[i] = sub
	}

	for i := 1; i < rs1Len+1; i++ {
		for j := 1; j < rs2Len+1; j++ {
			d1 := arr[i-1][j] + 1
			d2 := arr[i][j-1] + 1

			n := 0
			if rs1[i-1] != rs2[j-1] {
				n = 1
			}

			d3 := arr[i-1][j-1] + n
			arr[i][j] = math.Min(d1, d2, d3)

		}
	}

	return arr[rs1Len][rs2Len]
}

func main() {
	Levenshtein("sunda", "sund")

}
