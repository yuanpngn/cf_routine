# Emergency Landing Feature

## Overview
The drone choreography system now includes an emergency landing feature that allows the operator to safely land the drone at any time during the performance by pressing any key on the keyboard.

## How It Works

### Keyboard Monitoring
- The system continuously monitors for keyboard input during all movements
- Checking happens every 0.1 seconds (non-blocking)
- Works on macOS, Linux, and Windows platforms

### Emergency Landing Process
When any key is pressed:

1. **Immediate Detection**: The system detects the keyboard input within 0.1 seconds
2. **Stop Current Command**: Sends stop command to the high-level commander
3. **Height Tracking**: Uses the last known height to calculate safe landing
4. **Smooth Descent**: Performs controlled landing at safe velocity (0.25 m/s)
5. **Safe Disarm**: Properly disarms the drone after landing

### Safety Features

- **Smooth Landing**: Uses the same descent velocity as normal landing (0.25 m/s)
- **Height Awareness**: Tracks current height throughout the performance
- **Graceful Degradation**: Multiple fallback mechanisms if landing fails
- **No Abrupt Stops**: All emergency landings are controlled descents

## Usage

1. **Start the Performance**: Run `python3 main.py`
2. **Monitor the Drone**: Watch the performance
3. **Emergency Stop**: Press any key on the keyboard if needed
4. **Wait for Landing**: Let the system complete the smooth landing

## User Feedback

When the script starts:
```
[ARM] Armed.
[INFO] Press any key at any time to initiate emergency smooth landing...
```

When emergency landing is triggered:
```
[EMERGENCY] Keyboard input detected — initiating smooth emergency landing...
[EMERGENCY] Landing from approximately 1.50m...
[EMERGENCY] Emergency landing completed.
[DISARM] Disarmed.
```

## Technical Details

### Height Tracking Points
The system tracks height at key moments:
- After takeoff: 1.5m
- During diagonal movements: 1.2m - 2.4m
- After spiral: 2.0m → 1.5m
- Standard flight: 1.5m
- After landing: 0.0m

### Keyboard Input Detection
- **macOS/Linux**: Uses `select.select()` for non-blocking input
- **Windows**: Uses `msvcrt.kbhit()` for keyboard detection
- Check interval: 100ms (0.1 seconds)

### Movement Functions with Monitoring
All timed movements include keyboard checking:
- `goto()` - Main movement function
- `safe_sleep()` - Monitored sleep function
- Diagonal movement loops
- All sleep calls during choreography

## Code Structure

```python
# Global tracking
emergency_stop = False
current_height = 0.0

# Monitoring function
def check_keyboard_input():
    # Platform-specific keyboard detection
    
# Safe movement with monitoring
def goto(hl, xy, z, dur):
    # Execute movement
    # Check keyboard every 0.1s
    
# Exception handling
except KeyboardInterrupt:
    # Stop commands
    # Calculate height
    # Perform smooth landing
```

## Important Notes

⚠️ **Best Practices:**
- Always keep eyes on the drone during flight
- Only use emergency landing when necessary
- Let the landing complete - don't interrupt it
- Ensure clear landing space below drone

✅ **What Emergency Landing Does:**
- Stops current movement command
- Descends at safe velocity (0.25 m/s)
- Properly disarms motors

❌ **What Emergency Landing Does NOT Do:**
- No instant motor cutoff (that would crash)
- No horizontal repositioning (lands from current position)
- Cannot be cancelled once initiated

## Testing

Before using in performance:
1. Test emergency landing from different heights
2. Verify smooth descent
3. Check that drone lands stably
4. Confirm proper disarm sequence

## Future Enhancements

Potential improvements:
- Audio feedback for emergency landing
- LED indicators during emergency
- Log emergency events
- Return-to-home option instead of immediate landing
