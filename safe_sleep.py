# safe_sleep.py
import sys, select, time

# Global flag to signal an emergency stop
emergency_stop = False

def check_keyboard_input():
    """
    Check if any keyboard input is available (non-blocking).
    Sets the global emergency_stop flag if input is detected.
    """
    global emergency_stop
    if emergency_stop:  # Don't check again if already triggered
        return True

    if sys.platform == 'win32':
        import msvcrt
        if msvcrt.kbhit():
            emergency_stop = True
            return True
    else:
        # Unix/Linux/Mac
        if select.select([sys.stdin], [], [], 0)[0] != []:
            emergency_stop = True
            return True
    return False

def safe_sleep(duration):
    """
    Sleep for a given duration while checking for keyboard input.
    Raises KeyboardInterrupt if input is detected.
    """
    global emergency_stop
    elapsed = 0
    interval = 0.1
    
    while elapsed < duration:
        if check_keyboard_input():
            emergency_stop = True
            raise KeyboardInterrupt("Keyboard input detected - initiating smooth landing")
        
        time.sleep(min(interval, duration - elapsed))
        elapsed += interval

def get_emergency_flag():
    """Allows other modules to check the flag"""
    global emergency_stop
    return emergency_stop