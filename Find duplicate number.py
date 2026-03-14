def find_duplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return n
        seen.add(n)
