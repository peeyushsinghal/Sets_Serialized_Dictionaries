from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts) -> dict:
    """
    Merges multiple dictionaries using defaultdict, combining frequencies
    and sorting by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        dict: Merged dictionary sorted by frequency in descending order
    """
    if not dicts:
        return {}
    
    # Create defaultdict to accumulate frequencies
    merged = defaultdict(int)
    
    # Merge all dictionaries
    for d in dicts:
        for word, freq in d.items():
            merged[word] += freq
    
    # Convert to regular dict and sort by frequency
    result = dict(sorted(
        merged.items(),
        key=lambda x: (-x[1], x[0])  # Sort by frequency desc, then word asc
    ))
    
    return result

def merge_with_counter(*dicts) -> dict:
    """
    Merges multiple dictionaries using Counter, combining frequencies
    and sorting by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries to merge
        
    Returns:
        dict: Merged dictionary sorted by frequency in descending order
    """
    if not dicts:
        return {}
    
    # Create Counter objects and sum them
    merged = Counter()
    for d in dicts:
        merged.update(d)
    
    # Sort by frequency and convert to regular dict
    result = dict(sorted(
        merged.items(),
        key=lambda x: (-x[1], x[0])  # Sort by frequency desc, then word asc
    ))
    
    return result 