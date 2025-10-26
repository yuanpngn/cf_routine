from safe_sleep import safe_sleep

def hover(_hl, duration_s=2.0):
    # HL commander holds last setpoint; we just wait.
    safe_sleep(max(0.0, duration_s))