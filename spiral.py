import time, math
from cfutils import hl_go_to_compat, face_center_yaw_deg

def spiral_arc(hl, *, cx=0.0, cy=0.0,
               z_start=1.5, z_end=2.0,
               radius=0.8, segments=24, seg_t=1.0,
               face_center=True, world_yaw_offset_deg=0.0):
    """
    Ascends (or descends) while orbiting around (cx, cy).
    """
    for k in range(segments + 1):
        t = k / float(segments)
        angle = 2.0 * math.pi * t
        z = z_start + (z_end - z_start) * t
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        yaw_deg = (face_center_yaw_deg(x, y, cx, cy, world_yaw_offset_deg)
                   if face_center else None)
        hl_go_to_compat(hl, x, y, z, yaw_deg=yaw_deg, duration_s=seg_t, relative=False)
        time.sleep(seg_t + 0.0)