import numpy as np

def calculate_angle(a,b,c):
    """
    Calculate the angle at point b formed by points a and c using the law of cosines.
    
    Parameters:
    a (tuple): Coordinates of point a (x1, y1).
    b (tuple): Coordinates of point b (x2, y2).
    c (tuple): Coordinates of point c (x3, y3).
    
    Returns:
    float: Angle at point b in degrees.
    """
    # Convert points to numpy arrays for easier calculations
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    # Use vector dot-product formula for the angle at point b between (a-b) and (c-b)
    v1 = a - b
    v2 = c - b

    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    # Handle degenerate zero-length vectors
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0

    cos_angle = np.dot(v1, v2) / (norm_v1 * norm_v2)
    cos_angle = np.clip(cos_angle, -1.0, 1.0)

    angle_rad = np.arccos(cos_angle)
    # Convert radians to degrees
    angle_deg = np.degrees(angle_rad)
    return angle_deg

def asses_posture(key_points):
    """
    Returns posture risk :normal /risky /critical
    usin shouler-hip-knee angle
    """
    try:
        left_shoulder = key_points[5]
        left_hip = key_points[11]
        left_knee = key_points[13]      

        right_shoulder = key_points[6]
        right_hip = key_points[12]
        right_knee = key_points[14]

        left_angle=calculate_angle(left_shoulder, left_hip, left_knee)
        right_angle=calculate_angle(right_shoulder, right_hip, right_knee)  
        avg_angle=(left_angle+right_angle)/2

        if avg_angle>160:
            return "normal"
        elif avg_angle>120:
            return "risky"
        else:
            return "critical"       

    except Exception:
        return "unknown"
    

def assess_posture(key_points):
    """
    Backwards-compatible wrapper with the correct spelling.
    Calls the existing `asses_posture` implementation.
    """
    return asses_posture(key_points)
    
