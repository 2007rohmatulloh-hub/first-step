def rearrange_by_frequency(nums: list[int]) -> list[int]:
    from collections import Counter
    fre = Counter(nums) 

    new  = []

    for num1, num2 in sorted(fre.items(), key=lambda x: (-x[1], x[0])):
        # print(num2)
        new.extend([num1]* num2)
    return new
print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
# Kutilgan natija: [4, 4, 4, 5, 5, 3, 6]