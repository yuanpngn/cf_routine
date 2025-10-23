from cfutils import hl_land_compat
import time

def land(hl, from_height_m=1.5, descent_vel=0.125):
    hl_land_compat(hl, from_height_m, descent_vel)
    time.sleep(max(2.0, from_height_m / max(0.1, descent_vel)) + 0.3)
    try:
        hl.stop()
    except Exception:
        pass