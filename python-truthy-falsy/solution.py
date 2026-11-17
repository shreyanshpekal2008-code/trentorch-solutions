def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    
    if ( value is None or value is False or value == 0.00 ):
        return False
    if isinstance(value, (str, list, tuple, dict, set)) and len(value) == 0:
        return False 
            
                                                                                
    else :
        return True
    pass


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for i in values:
        if(is_truthy(i)==True):
            return i
    return None
    pass
