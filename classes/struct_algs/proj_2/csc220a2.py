"""Module providing a function to flatten a nested list or tuple."""

def flatten(user_input):
    """
    Recursively flattens a nested list or tuple.
    
    Args:
    user_input: A list or tuple, potentially nested with other lists or tuples.
    
    Returns:
    A flattened tuple of all elements.
    """
    flat_tuple = ()

    for item in user_input:
        if isinstance(item, (list, tuple)):
            flat_tuple += flatten(item)
        else:
            flat_tuple += (item,)

    return flat_tuple
