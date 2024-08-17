package go_lang

import (
	"sort"
)

func BoatsToSave(people []int, limit int) int {

	noOfBoats := 0
	left := 0
	right := len(people) - 1

	sort.Ints(people)
	for left < right {
		noOfBoats += 1
		sumOfWeights := people[left] + people[right]
		if sumOfWeights == limit {
			left += 1
			right -= 1
		} else if sumOfWeights > limit {
			right -= 1
		} else if sumOfWeights < limit {
			left += 1
			right -= 1
		}
	}

	if left == right {
		noOfBoats += 1
	}
	return noOfBoats
}
