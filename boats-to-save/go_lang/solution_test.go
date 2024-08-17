package go_lang

import "testing"

func TestBoatsToSave01(t *testing.T) {
	want := 3
	limit := 3
	people_weights := []int{3, 2, 1, 2}
	got := BoatsToSave(people_weights, limit)
	if got != want {
		t.Errorf("got %v want %v", got, want)
	}
}

func TestBoatsToSave02(t *testing.T) {
	want := 4
	limit := 5
	people_weights := []int{3, 5, 3, 4}
	got := BoatsToSave(people_weights, limit)
	if got != want {
		t.Errorf("got %v want %v", got, want)
	}
}

func TestBoatsToSave03(t *testing.T) {
	want := 1
	limit := 3
	people_weights := []int{1, 2}
	got := BoatsToSave(people_weights, limit)
	if got != want {
		t.Errorf("got %v want %v", got, want)
	}
}
