import numpy as np

def replace_outliers_with_median(data, outliers):
    """
    Replace outliers in the input data with the median value.
    
    Parameters:
        data (array-like): Input data (e.g., array of heartbeats).
        outliers (list): List of indices corresponding to outlier data points.
    
    Returns:
        cleaned_data (array-like): Data with outliers replaced by the median.
    """
    cleaned_data = data.copy()
    median_value = np.median(data)
    
    for idx in outliers:
        cleaned_data[idx] = median_value
    
    return cleaned_data
