class SearchingAlgorithms:
    def linear_search(self, input_array, searched_element):
        for x in input_array:
            if searched_element == x:
                return True
        return False
