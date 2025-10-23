from cfutils import hl_takeoff_compat
import time

def takeoff(hl, height_m=1.5, ascent_vel=0.6):
    hl_takeoff_compat(hl, height_m, ascent_vel)
    # leave enough time to climb and stabilize
    time.sleep(max(1.0, height_m / max(0.1, ascent_vel)) + 0.3)