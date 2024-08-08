package main

import (
	"fmt"
	"math"
)

func max_area(driver []float64) int {
	maxArea := float64(0)
	left := 0
	right := len(driver) - 1
	for left < right {
		area := float64((right - left)) * math.Min(driver[left], driver[right])
		maxArea = math.Max(maxArea, area)
		if driver[left] > driver[right] {
			right -= 1
		} else {
			left += 1
		}
	}
	return int(maxArea)
}

func main() {
	driver := []float64{2, 3, 4, 5, 18, 17, 6}
	m := max_area(driver)
	fmt.Println(fmt.Sprintf("max area is %d", m))

}
