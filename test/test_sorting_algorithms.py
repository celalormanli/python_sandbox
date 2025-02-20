from src.sorting_algorithms import SortingAlgorithms


def test_sorting_algorithims_selection_sort():
    sorting_algorithims = SortingAlgorithms()
    assert sorting_algorithims.selection_short([10, 8, 48]) == [8, 10, 48]
    assert sorting_algorithims.selection_short(
        [10, 8, 48, 1]) == [1, 8, 10, 48]


def test_sorting_algorithims_bubble_sort():
    sorting_algorithims = SortingAlgorithms()
    assert sorting_algorithims.bubble_sort([10, 8, 48]) == [8, 10, 48]
    assert sorting_algorithims.bubble_sort([10, 8, 48, 1]) == [1, 8, 10, 48]
    assert sorting_algorithims.bubble_sort([-1, 2, 3, 4]) == [-1, 2, 3, 4]


def test_sorting_algorithims_recursive_bubble_sort():
    sorting_algorithims = SortingAlgorithms()
    assert sorting_algorithims.recursive_bubble_sort([10, 8, 48]) == [
        8, 10, 48]
    assert sorting_algorithims.recursive_bubble_sort([10, 8, 48, 1]) == [
        1, 8, 10, 48]
    assert sorting_algorithims.recursive_bubble_sort(
        [-1, 2, 3, 4]) == [-1, 2, 3, 4]


def test_sorting_algorithims_insertion_sort():
    sorting_algorithims = SortingAlgorithms()
    assert sorting_algorithims.insertion_sort([10, 8, 48]) == [
        8, 10, 48]
    assert sorting_algorithims.insertion_sort([10, 8, 48, 1]) == [
        1, 8, 10, 48]
    assert sorting_algorithims.insertion_sort(
        [-1, 2, 3, 4]) == [-1, 2, 3, 4]


def test_sorting_algorithims_heap_sort():
    sorting_algorithims = SortingAlgorithms()
    assert sorting_algorithims.heap_sort([10, 8, 48]) == [
        8, 10, 48]
    assert sorting_algorithims.heap_sort([10, 8, 48, 1]) == [
        1, 8, 10, 48]
    assert sorting_algorithims.heap_sort(
        [-1, 2, 3, 4]) == [-1, 2, 3, 4]
