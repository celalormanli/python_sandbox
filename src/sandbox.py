class Sandbox:
    def fibonacci(self, x):
        if x <= 1:
            return x
        return self.fibonacci(x-1) + self.fibonacci(x-2)

    def tower_of_hanoi(self, height,
                       from_pole, to_pole, with_pole):
        if height >= 1:
            self.tower_of_hanoi(height-1, from_pole,
                                with_pole, to_pole)
            to_pole.append(from_pole.pop())
            self.tower_of_hanoi(height-1, with_pole,
                                to_pole, from_pole)
