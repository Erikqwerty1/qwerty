def min_max(nums):
    if len(nums) == 0:
        raise ValueError
    a = min(nums)
    b = max(nums)
    return (a, b)
nums = [3, -1, 5, 5, 0]
print(min_max(nums)) 
nums = [42]
print(min_max(nums))
nums = [-5, -2, -9]
print(min_max(nums))
nums = [1.5, 2, 2.0, -3.1]
print(min_max(nums))
nums = []
print(min_max(nums))
