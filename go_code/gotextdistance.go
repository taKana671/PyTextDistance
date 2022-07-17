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
	if s1 == s2 {
		return 0
	}
	rs1 := []rune(s1)
	rs2 := []rune(s2)

	return levenshteinDistance(rs1, rs2)

}

//export NormalizedLevenshtein
func NormalizedLevenshtein(s1 string, s2 string) float64 {
	if s1 == s2 {
		return 0.0
	}
	rs1 := []rune(s1)
	rs2 := []rune(s2)
	distance := float64(levenshteinDistance(rs1, rs2))
	maxLen := float64(max([]int{len(rs1), len(rs2)}))

	return distance / maxLen
}

func levenshteinDistance(rs1 []rune, rs2 []rune) int {
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

//export DamerauLevenshtein
func DamerauLevenshtein(s1 string, s2 string) int {
	if s1 == s2 {
		return 0
	}

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
			arr[i][j] = min([]int{
				arr[i][j-1] + 1,
				arr[i-1][j] + 1,
				arr[i-1][j-1] + cost,
				arr[k-1][l-1] + max([]int{i - k - 1, j - l - 1}) + 1,
			})

		}
		m[rs1[i-2]] = i
	}
	return arr[rs1Len+1][rs2Len+1]
}

//export JaroWinkler
func JaroWinkler(s1 string, s2 string) float64 {
	jaro_distance := Jaro(s1, s2)

	if jaro_distance > 0.7 {
		rs1 := []rune(s1)
		rs2 := []rune(s2)
		prefix := 0
		limit := min([]int{len(rs1), len(rs2)})

		for i := 0; i < limit; i++ {
			if rs1[i] == rs2[i] {
				prefix += 1
			} else {
				break
			}
		}
		prefix = min([]int{4, prefix})
		jaro_distance += 0.1 * float64(prefix) * (1 - jaro_distance)

	}
	return jaro_distance
}

//export Jaro
func Jaro(s1 string, s2 string) float64 {
	if s1 == s2 {
		return 1.0
	}

	rs1 := []rune(s1)
	rs2 := []rune(s2)
	rs1Len := len(rs1)
	rs2Len := len(rs2)

	if rs1Len == 0 || rs2Len == 0 {
		return 0.0
	}
	if rs1Len > rs2Len {
		rs1, rs2 = rs2, rs1
		rs1Len, rs2Len = rs2Len, rs1Len
	}

	search_range := int((rs1Len + 1) / 2)
	match := 0.0
	rs1Match := make([]int, rs1Len)
	rs2Match := make([]int, rs2Len)

	for i := 0; i < rs1Len; i++ {
		start := max([]int{0, i - search_range})
		end := min([]int{rs2Len, i + search_range + 1})
		for j := start; j < end; j++ {
			if rs1[i] == rs2[j] && rs2Match[j] == 0 {
				rs1Match[i] = 1
				rs2Match[j] = 1
				match += 1.0
				break
			}
		}
	}

	if match == 0 {
		return 0.0
	}

	trans := 0.0
	k := 0
	for i := 0; i < rs1Len; i++ {
		if rs1Match[i] != 0 {
			for {
				if rs2Match[k] != 0 {
					break
				}
				k += 1
			}
			if rs1[i] != rs2[k] {
				k += 1
				trans += 1.0
			} else {
				k += 1
			}
		}
	}
	trans = trans / 2.0
	return (match/float64(rs1Len) + match/float64(rs2Len) + (match-trans)/match) / 3.0

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

func main() {}
