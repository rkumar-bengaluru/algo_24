package go_movezeroes

import (
	"reflect"
	"testing"
)

func TestMoveZeroes_01(t *testing.T) {
	nums := []int{0, 1, 0, 3, 12}
	want := []int{1, 3, 12, 0, 0}

	MoveZeroes(nums)
	if !reflect.DeepEqual(nums, want) {
		t.Errorf("got %v want %v", nums, want)
	}
}
