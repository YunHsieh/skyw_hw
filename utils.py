
def to_nums(data: str) -> list[int]:
    """
    str convert to list
    for example:
        '1 2 3' -> [1, 2, 3]
    """
    nums = []
    for i in data.split(' '):
        if not i.isdigit():
            return []
        nums.append(int(i))
    return nums
