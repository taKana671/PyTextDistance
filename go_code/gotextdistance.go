package main

import "C"

//export hamming
func hamming(s1 string, s2 string) int {
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

func main() {}
