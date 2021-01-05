class SortingAlgorithms:
    def selection_short(self, input_array):
        for x in range(len(input_array)):
            min_num_ind = x
            for y in range(x, len(input_array)):
                if input_array[min_num_ind] > input_array[y]:
                    min_num_ind = y
            temp = input_array[x]
            input_array[x] = input_array[min_num_ind]
            input_array[min_num_ind] = temp
        return input_array

    def bubble_sort(self, input_array):
        for x in range(len(input_array) - 1):
            for y in range(len(input_array) - x - 1):
                if input_array[y] > input_array[y + 1]:
                    temp = input_array[y]
                    input_array[y] = input_array[y + 1]
                    input_array[y + 1] = temp
        return input_array

    def recursive_bubble_sort(self, input_array, counter=None):
        if counter is None:
            counter = len(input_array)
        if counter == 1:
            return input_array
        for x in range(counter - 1):
            if input_array[x] > input_array[x + 1]:
                input_array[x], input_array[x + \
                    1] = input_array[x + 1], input_array[x]
        self.recursive_bubble_sort(input_array, (counter - 1))
        return input_array
