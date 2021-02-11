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


def test_depth_first_search():
    graph = {'A': ['B', 'E'],
             'B': ['D', 'C'],
             'C': ['B', 'D'],
             'D': ['B', 'C'],
             'E': ['F'],
             'F': []}
    searching_algorithms = SearchingAlgorithms()
    visited = []
    visited = searching_algorithms.depth_first_search(graph, 'A')
    assert visited == ['A', 'E', 'F', 'B', 'C', 'D']


def test_breadth_first_search():
    graph = {'A': ['B', 'E'],
             'B': ['D', 'C'],
             'C': ['B', 'D'],
             'D': ['B', 'C'],
             'E': ['F'],
             'F': []}
    searching_algorithms = SearchingAlgorithms()
    visited = []
    visited = searching_algorithms.breadth_first_search(graph, 'A')
    assert visited == ['A', 'B', 'E', 'D', 'C', 'F']


def test_jump_search():
    searching_algorithms = SearchingAlgorithms()
    input_array = [0, 1, 1, 2, 3, 5,
                   8, 13, 21, 34, 55,
                   89, 144, 233, 377, 610]
    index = searching_algorithms.jump_search(input_array, 21)
    assert index == 8
    index = searching_algorithms.jump_search(input_array, 22)
    assert index == -1
