import time

def hover(_hl, duration_s=2.0):
    # HL commander holds last setpoint; we just wait.
    time.sleep(max(0.0, duration_s))