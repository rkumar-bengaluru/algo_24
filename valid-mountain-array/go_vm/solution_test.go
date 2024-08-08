package go_vm

import (
	"testing"
)

func TestValidMountain(t *testing.T) {
	driver := []int16{1, 2, 3}
	got := validMountain(driver)
	want := false
	if got != want {
		t.Errorf("got %v, expected %v", got, want)
	}
}
