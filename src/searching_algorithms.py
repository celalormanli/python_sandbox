class SearchingAlgorithms:
    def linear_search(self, input_array, searched_element):
        for x in input_array:
            if searched_element == x:
                return True
        return False

    def binary_search(self, input_array, le, ri, x):
        while le <= ri:
            mid = le + (ri - 1) // 2

            if input_array[mid] == x:
                return True
            elif input_array[mid] < x:
                le = mid + 1
            else:
                ri = mid - 1

        return False
