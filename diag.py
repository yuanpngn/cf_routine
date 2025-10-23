from cfutils import hl_move_distance_compat
import time

def diag(hl, dx=0.4, dy=0.4, dz=0.0, duration_s=2.0):
    hl_move_distance_compat(hl, dx, dy, dz, duration_s=duration_s)
    time.sleep(duration_s + 0.05)