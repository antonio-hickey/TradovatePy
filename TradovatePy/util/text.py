def multi_ids(array: list[int]) -> str:
    """Convert multiple ids to string"""
    return ','.join(str(i) for i in array)
