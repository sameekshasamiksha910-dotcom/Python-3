class Fibonacci:
    def __init__(self, n):
        self.n = n

    def dynamic(self):
        a, b = 0, 1

        for i in range(self.n):
            a, b = b, a + b

        return a


if __name__ == "__main__":
    num = int(input("Enter n: "))
    fib = Fibonacci(num)

    print(f"Fib({num}) = {fib.dynamic()}")