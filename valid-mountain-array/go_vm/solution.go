package go_vm

import (
	"fmt"
)

/**
** Given an array of integer arr return true if and only if it is a valid mountain array
** Recall that arr is a mountain array if
**     * arr.length >= 3
**     * There exist some i with 0 < i < arr.length -1 such that,
**          * arr[0] < arr[1] < .... < arr[i -1] < arr[i]
**          * arr[0] > arr[1] > .... > arr[arr.length -1]
 */
func validMountain(arr []int16) bool {
	if len(arr) < 3 {
		return false
	}
	i := 1
	for i < len(arr) {
		if arr[i] <= arr[i-1] {
			break
		}
		i += 1
	}
	if i == len(arr) || i == 1 {
		return false
	}
	for i < len(arr) {
		if arr[i] >= arr[i-1] {
			break
		}
		i += 1
	}
	return i == len(arr)
}

func main() {
	driver := []int16{1, 2, 3}
	fmt.Println(validMountain(driver))
}
