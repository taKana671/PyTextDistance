package main

import "C"
import "fmt"

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

	arr := make([][]uint, rs1Len+1)

	for i := range arr {
		sub := make([]uint, rs2Len+1)
		if i == 0 {
			for j := range sub {
				sub[j] = uint(j)
			}
		} else {
			sub[0] = uint(i)
		}
		arr[i] = sub
	}

	fmt.Println(arr)
	return rs2Len
}

func main() {
	Levenshtein("sunda", "sund")

}
