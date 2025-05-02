import pandas as pd

def validate_input(input_dict, feature_names):
    """
    Validate and clean input data
    """
    cleaned_input = input_dict.copy()
    
    for feature in feature_names:
        if feature not in cleaned_input:
            raise ValueError(f"Missing required feature: {feature}")
        
        try:
            cleaned_input[feature] = int(cleaned_input[feature])
        except (ValueError, TypeError):
            raise ValueError(f"Invalid value for {feature}")
    
    input_df = pd.DataFrame([
        [cleaned_input.get(feature, 0) for feature in feature_names]
    ], columns=feature_names)
    
    return input_df

def prepare_input_data(input_dict, feature_names):
    """
    Prepare input data for prediction with additional validation
    """
    try:
        input_df = validate_input(input_dict, feature_names)
        return input_df
    except Exception as e:
        raise ValueError(f"Input validation error: {str(e)}")