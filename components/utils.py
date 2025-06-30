from random import randint


def generate_id_list(amount: int, range: tuple[int,int]) -> list[int]:
    """Generate a list of unique random IDs within a specified range.

    Args:
        amount (int): The number of unique IDs to generate.
        range (tuple[int, int]): The range (inclusive) from which to generate IDs.

    Returns:
        list[int]: A list of unique IDs.
    """
    
    if amount > (range[1] - range[0] + 1):
        raise ValueError("Amount exceeds the range of unique IDs available.")
    
    ids = set()
    while len(ids) < amount:
        id = randint(range[0], range[1])
        if id not in ids:
            ids.add(id)
    return list(ids)
