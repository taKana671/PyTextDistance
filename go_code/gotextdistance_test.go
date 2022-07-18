package main

import "testing"

func TestHamming(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect int
	}{
		{"karolin", "kathrin", 3},
		{"karolin", "kerstin", 3},
		{"kathrin", "kerstin", 4},
		{"1011101", "1001001", 2},
		{"2173896", "2233796", 3},
		{"Brian", "Jesus", 5},
		{"Brian", "Brian", 0},
		{"アイス", "ミント", 3},
		{"dixon", "dickson", -1},
		{"だんす", "だん", -1},
	}

	for _, test := range tests {
		result := Hamming(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("Hamming: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}

}

func TestLevenshtein(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect int
	}{
		{"sitting", "kitten", 3},
		{"sunday", "saturday", 3},
		{"", "", 0},
		{"sitting", "", 7},
		{"aabcc", "bccdd", 4},
		{"idカード", "Id番号カード", 3},
		{"ひだるま", "けんだま", 3},
		{"山田太郎", "山田太郎", 0},
	}

	for _, test := range tests {
		result := Levenshtein(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("Levenshtein: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}

}

func TestNormalizedLevenshtein(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect float64
	}{
		{"アイス", "ミント", 1.0},
		{"チョコレート", "チョコレートアイス", 0.3333333333333333},
		{"dixon", "dickson", 0.42857142857142855},
		{"sunday", "saturday", 0.375},
		{"山田太郎", "山田太郎", 0},
	}

	for _, test := range tests {
		result := NormalizedLevenshtein(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("NormalizedLevenshtein: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}
}

func TestDamerauLevenshtein(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect int
	}{
		{"abcdef", "abcfad", 2},
		{"ca", "abc", 2},
		{"a cat", "a abct", 2},
		{"a cat", "an act", 2},
		{"ifhs", "fish", 2},
		{"BADC", "ABCD", 2},
		{"ZX", "XYZ", 2},
		{"BADC", "", 4},
		{"", "ABCD", 4},
		{"ABCD", "ABCD", 0},
		{"", "", 0},
		{"idカード", "Id番号", 4},
	}

	for _, test := range tests {
		result := DamerauLevenshtein(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("DamerauLevenshtein: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}
}

func TestJaroWinkler(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect float64
	}{
		{"abc", "bac", 0.8888888888888888},
		{"dicksonx", "dixon", 0.8133333333333332},
		{"dixon", "dicksonx", 0.8133333333333332},
		{"Brian", "Jesus", 0.0},
		{"Thorkel", "Thorgier", 0.8678571428571429},
		{"Dinsdale", "D", 0.7375},
		{"Carol", "elephant", 0.44166666666666665},
		{"", "", 1.0},
		{"Dinsdale", "", 0.0},
		{"", "elephant", 0.0},
		{"idカード", "Id番号", 0.48333333333333334},
		{"ひだるま", "けんだま", 0.6666666666666666},
	}

	for _, test := range tests {
		result := JaroWinkler(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("JaroWinkler: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}
}

func TestJaro(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect float64
	}{
		{"abc", "bac", 0.8888888888888888},
		{"dicksonx", "dixon", 0.7666666666666666},
		{"dixon", "dicksonx", 0.7666666666666666},
		{"Brian", "Jesus", 0.0},
		{"Thorkel", "Thorgier", 0.7797619047619048},
		{"Dinsdale", "D", 0.7083333333333334},
		{"Carol", "elephant", 0.44166666666666665},
		{"", "", 1.0},
		{"Dinsdale", "", 0.0},
		{"", "elephant", 0.0},
		{"idカード", "Id番号", 0.48333333333333334},
		{"ひだるま", "けんだま", 0.6666666666666666},
	}

	for _, test := range tests {
		result := Jaro(test.s1, test.s2)
		if result != test.expect {
			t.Errorf("Jaro: [s1]%v [s2]%v [expect]%v [result]%v", test.s1, test.s2, test.expect, result)
		}
	}
}
