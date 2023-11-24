def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    final_sum = 0
    if not end:
        for i in range(start,len(nums),1):
            final_sum += nums[i]
    else:
        if end < len(nums):
            for i in range(start,end+1,1):
                final_sum += nums[i]
        elif end == len(nums):
            for i in range(start,end,1):
                final_sum += nums[i]
        else:
            for i in range(start,len(nums),1):
                final_sum += nums[i]
    return final_sum
