class Sandbox:
    def fibonacci(self, x):
        if x <= 1:
            return x
        return self.fibonacci(x-1) + self.fibonacci(x-2)
