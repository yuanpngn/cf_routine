import time, math
from cfutils import hl_go_to_compat, face_center_yaw_deg

def horizontal_figure8(hl, *, cx=0.0, cy=1.0, z=1.5,
                       width=1.2, height_var=0.3,
                       total_time=30.0, segments=60,
                       face_center=True, world_yaw_offset_deg=0.0):
    """
    Draws a horizontal figure-8 (lemniscate) pattern in front of the dancer.
    Creates overlapping circles in the horizontal plane with slight height variation.
    
    Args:
        cx, cy: Center point of the figure-8 (typically center front)
        z: Base height
        width: Width of the figure-8 (left-right extent)
        height_var: Height variation during the pattern
        total_time: Total duration
        segments: Number of points in the path
        face_center: If True, always face performer at (0, 0)
        world_yaw_offset_deg: Additional yaw offset
    """
    dt = max(0.02, total_time / float(segments))
    
    for k in range(segments + 1):
        t = k / float(segments)
        angle = 2.0 * math.pi * t
        
        # Lemniscate (figure-8) parametric equations
        # x(t) = a * cos(t) / (1 + sin²(t))
        # y(t) = a * sin(t) * cos(t) / (1 + sin²(t))
        # Simplified form for smooth figure-8:
        sin_t = math.sin(angle)
        cos_t = math.cos(angle)
        
        # Horizontal figure-8 shape
        px = cx + (width / 2.0) * sin_t * cos_t / (1.0 + 0.3 * sin_t * sin_t)
        py = cy + (width / 3.0) * cos_t
        
        # Add slight height variation for visual interest
        pz = z + height_var * math.sin(2.0 * angle)
        
        # Face the performer at (0, 0) or maintain yaw
        yaw_deg = (face_center_yaw_deg(px, py, 0.0, 0.0, world_yaw_offset_deg)
                   if face_center else None)
        
        hl_go_to_compat(hl, px, py, pz, yaw_deg=yaw_deg, duration_s=dt, relative=False)
        time.sleep(dt)


def spiral_arc(hl, *, cx=0.0, cy=0.0,
               z_start=1.5, z_end=2.0,
               radius=0.8, segments=24, seg_t=1.0,
               face_center=True, world_yaw_offset_deg=0.0):
    """
    Ascends (or descends) while orbiting around (cx, cy).
    Vertical spiral motion.
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
