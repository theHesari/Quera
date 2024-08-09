class Chain:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        if isinstance(self.value, (int, float)) and isinstance(other, (int, float)):
            # Sum of numbers
            return Chain(self.value + other)
        elif isinstance(self.value, str) and isinstance(other, str):
            # Concatenation with space
            return Chain(f"{self.value} {other}")
        else:
            # Raise exception for invalid operations
            raise Exception("invalid operation")

    def __eq__(self, other):
        if isinstance(other, Chain):
            return self.value == other.value
        return self.value == other

    def __str__(self):
        # Return the string representation of the final result
        return str(self.value)

    def __repr__(self):
        # For better representation in the shell
        if isinstance(self.value, str):
            return f"'{self.value}'"
        return f"{self.value}"


if __name__ == "__main__":
    # Example usage:
    print(Chain(2.5)(2)(2)(2.5))  # Output: 9
    print(Chain(3)(1.5)(2)(3))  # Output: 9.5
    print(Chain(64) == 64)  # Output: True
    print(Chain('Ali')('Safinal')('is')('the')('best.'))  # Output: 'Ali Safinal is the best.'
    print(Chain('abc')('defg') == 'abc defg')  # Output: True

    try:
        Chain('Ali')(5)
    except Exception as e:
        print(e)  # Output: invalid operation

    try:
        Chain(9)([1, 2])
    except Exception as e:
        print(e)  # Output: invalid operation
