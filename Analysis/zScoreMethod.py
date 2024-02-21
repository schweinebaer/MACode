import numpy as np

def detect_outliers_z_score(data, threshold=3):
    """
    Detect outliers in the input data using the Z-score method.
    
    Parameters:
        data (array-like): Input data (e.g., array of heartbeats).
        threshold (float): Z-score threshold for outlier detection.
    
    Returns:
        outliers (list): List of indices corresponding to outlier data points.
    """
    outliers = []
    mean = np.mean(data)
    std_dev = np.std(data)
    
    for i, x in enumerate(data):
        z_score = (x - mean) / std_dev
        if np.abs(z_score) > threshold:
            outliers.append(i)
    
    return outliers

