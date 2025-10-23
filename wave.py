import time, math
from cfutils import hl_go_to_compat, face_center_yaw_deg

def wave_orbit(hl, *, cx=0.0, cy=0.0,
               z_min=1.5, z_max=2.0,
               radius=0.8, total_time=30.0,
               cycles=3.0, segments=120,
               face_center=True, world_yaw_offset_deg=0.0):
    """
    Smooth orbit with vertical sine wave modulation between z_min and z_max.
    """
    dt = max(0.02, total_time / float(segments))
    amp = 0.5 * (z_max - z_min)
    zc  = 0.5 * (z_max + z_min)

    for k in range(segments + 1):
        t = k / float(segments)
        theta = 2.0 * math.pi * t
        z = zc + amp * math.sin(2.0 * math.pi * cycles * t)
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        yaw_deg = (face_center_yaw_deg(x, y, cx, cy, world_yaw_offset_deg)
                   if face_center else None)
        hl_go_to_compat(hl, x, y, z, yaw_deg=yaw_deg, duration_s=dt, relative=False)
        time.sleep(dt)

def sphere_gesture(hl, *, cx=0.0, cy=0.0,
                   z_center=1.5, radius=0.35,
                   total_time=8.0, segments=64,
                   face_center=True, world_yaw_offset_deg=0.0):
    """
    Smooth 3D 'sphere' impression:
    Parametric loxodrome-like sweep that fills a spherical loop and returns.
    """
    dt = max(0.02, total_time / float(segments))
    for k in range(segments + 1):
        t = k / float(segments)
        # Sweep latitude phi from -pi/2 to +pi/2 and back (sinusoid),
        # while theta spins faster to paint a spherical shell.
        phi = math.pi * (t - 0.5)  # -pi/2 .. +pi/2
        theta = 4.0 * math.pi * t  # two full spins
        lat_scale = math.cos(phi)
        x = cx + radius * lat_scale * math.cos(theta)
        y = cy + radius * lat_scale * math.sin(theta)
        z = z_center + radius * math.sin(phi)
        yaw_deg = (face_center_yaw_deg(x, y, cx, cy, world_yaw_offset_deg)
                   if face_center else None)
        hl_go_to_compat(hl, x, y, z, yaw_deg=yaw_deg, duration_s=dt, relative=False)
        time.sleep(dt)