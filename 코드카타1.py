def two_sum(nums, target):
    for x in range(0, len(nums)):
        for n in range(x+1, len(nums)):
            if nums[x] + nums[n] == target :
                return [x, n]