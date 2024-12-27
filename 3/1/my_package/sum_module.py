class SumCalculator:
    @staticmethod
    def calculate_sum(numbers):
        if not isinstance(numbers, list):
            raise ValueError("Input should be a list of numbers")
        return sum(numbers)