from src.searching_algorithms import SearchingAlgorithms


def test_linear_search():
    searching_algorithms = SearchingAlgorithms()
    assert searching_algorithms.linear_search([10, 8, 48], 5) is False
    assert searching_algorithms.linear_search([10, 8, 48], 48) is True


def test_binary_search():
    searching_algorithms = SearchingAlgorithms()
    assert searching_algorithms.binary_search(
        [8, 13, 58, 96, 101], 0, 4, 5) is False
    assert searching_algorithms.binary_search(
        [8, 13, 58, 96, 101], 0, 4, 96) is True
