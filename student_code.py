def validate(data: dict, template: dict, path: str = '') -> tuple[bool, str]:
    """
    Validates a dictionary against a template.
    
    Args:
        data: Dictionary to validate
        template: Template to validate against
        path: Current path in the nested structure (used for error messages)
    
    Returns:
        Tuple of (bool, str) where:
        - bool indicates if validation passed
        - str contains error message if validation failed, empty string otherwise
    """
    # Check for missing or extra keys
    data_keys = set(data.keys())
    template_keys = set(template.keys())
    
    # Check for missing keys
    missing_keys = template_keys - data_keys
    if missing_keys:
        key = sorted(missing_keys)[0]
        return False, f'mismatched keys: {path + key if path else key}'
    
    # Check for extra keys
    extra_keys = data_keys - template_keys
    if extra_keys:
        key = sorted(extra_keys)[0]
        return False, f'mismatched keys: {path + key if path else key}'
    
    # Check types and nested structures
    for key, expected_type in template.items():
        current_path = f'{path}{key}' if path else key
        
        if isinstance(expected_type, dict):
            # Recursively validate nested dictionaries
            if not isinstance(data[key], dict):
                return False, f'bad type: {current_path}'
            
            state, error = validate(data[key], expected_type, f'{current_path}.')
            if not state:
                return False, error
        else:
            # Validate type of leaf values
            if data[key] is None or not isinstance(data[key], expected_type):
                return False, f'bad type: {current_path}'
    
    return True, '' 