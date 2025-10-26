from cfutils import hl_land_compat
from safe_sleep import safe_sleep

def land(hl, from_height_m=1.5, descent_vel=0.125):
    hl_land_compat(hl, from_height_m, descent_vel)
    safe_sleep(max(2.0, from_height_m / max(0.1, descent_vel)) + 0.3)
    try:
        hl.stop()
    except Exception:
        pass