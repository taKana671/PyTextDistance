package main

import "C"

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

//export Levenshtein
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
			arr[i][j] = min([]int{d1, d2, d3})

		}
	}
	return arr[rs1Len][rs2Len]
}

func DamerauLevenshtein(s1 string, s2 string) int {
	rs1 := []rune(s1)
	rs2 := []rune(s2)
	rs1Len := len(rs1)
	rs2Len := len(rs2)

	maxDist := rs1Len + rs2Len
	m := make(map[rune]int)

	arr := make([][]int, rs1Len+2)

	for i := range arr {
		sub := make([]int, rs2Len+2)
		for j := range sub {
			sub[j] = maxDist
		}
		arr[i] = sub
	}

	for i := 1; i < rs1Len+2; i++ {
		arr[i][1] = i - 1
	}
	for j := 1; j < rs2Len+2; j++ {
		arr[1][j] = j - 1
	}

	for i := 2; i < rs1Len+2; i++ {
		temp := 1
		for j := 2; j < rs2Len+2; j++ {
			k := m[rs2[j-2]]
			if _, ok := m[rs2[j-2]]; !ok {
				k = 1
			}
			l := temp
			cost := 1
			if rs1[i-2] == rs2[j-2] {
				cost = 0
			}
			if cost == 0 {
				temp = j
			}
			min([]int{
				arr[i][j-1] + 1,
				arr[i-1][j] + 1,
				arr[i-1][j-1] + cost,
				arr[k-1][l-1] + max([]int{i - k - 1, j - l - 1}) + 1,
			})

		}
		m[rs1[i-2]] = i
	}
	return arr[rs1Len+1][rs2Len+2]
}

func max(arr []int) int {
	max := arr[0]
	for _, n := range arr {
		if n > max {
			max = n
		}
	}
	return max
}

func min(arr []int) int {
	min := arr[0]
	for _, n := range arr {
		if n < min {
			min = n
		}
	}
	return min
}

// func min(n1 int, n2 int) int {
// 	if n1 <= n2 {
// 		return n1
// 	} else {
// 		return n2
// 	}
// }

func main() {}
