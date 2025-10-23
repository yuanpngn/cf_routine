from cfutils import hl_move_distance_compat
import time

def backward(hl, distance_m=0.5, duration_s=1.5):
    hl_move_distance_compat(hl, -distance_m, 0.0, 0.0, duration_s=duration_s)
    time.sleep(duration_s + 0.05)