"""Floc Exam 1"""
def main():
    """in main"""
    nums = [int(num) for num in input()[1:-1].split(',')]
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(nums[i] + result[len(result) - 1])
    print(result)
main()