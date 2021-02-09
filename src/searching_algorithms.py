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

    def depth_first_search(self, graph, start):
        stack = []
        visited = []
        stack.append(start)
        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                neighbourss = graph[node]
                for neighbour in neighbourss:
                    stack.append(neighbour)
        return visited

    def breadth_first_search(self, graph, start):
        visited = []
        queue = []
        queue.append(start)
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    queue.append(neighbour)
        return visited
