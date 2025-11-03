import math
from cfutils import hl_go_to_compat, face_center_yaw_deg
from safe_sleep import safe_sleep

def circle(hl, *, cx=0.0, cy=0.0, z=1.5, radius=1.2, total_time=20.0,
           segments=72, face_center=True, world_yaw_offset_deg=0.0, start_angle_deg=0.0):
    """
    Absolute CCW orbit around (cx,cy) at height z. Ends where it started.
    
    Args:
        start_angle_deg: Starting angle in degrees (0° = right, 90° = top/front, 180° = left, 270° = bottom/back)
    """
    dt = max(0.02, total_time / float(segments))
    start_angle_rad = math.radians(start_angle_deg)
    
    for k in range(segments + 1):
        theta = start_angle_rad + 2.0 * math.pi * (k / float(segments))
        px = cx + radius * math.cos(theta)
        py = cy + radius * math.sin(theta)
        yaw_deg = (face_center_yaw_deg(px, py, cx, cy, world_yaw_offset_deg)
                   if face_center else None)
        hl_go_to_compat(hl, px, py, z, yaw_deg=yaw_deg, duration_s=dt, relative=False)
        safe_sleep(dt)