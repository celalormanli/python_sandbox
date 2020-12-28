from src.searching_algorithms import SearchingAlgorithms

def test_linear_search():
    searching_algorithms = SearchingAlgorithms()
    assert searching_algorithms.linear_search([10,8,48],5)==False
    assert searching_algorithms.linear_search([10,8,48],48)==True