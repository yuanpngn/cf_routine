# Drone Orientation Guide

## Overview
The drone is programmed to **always face the performer** (located at origin 0, 0) during all movements. This ensures the camera/front of the drone points toward the performer throughout the choreography.

## Coordinate System Reminder

```
         +Y (Front/Audience)
          ↑
          |
    ------+------ +X (Right)
          |
          |
       Performer
       (0, 0)
```

## Drone Facing Direction at Key Positions

### 1. Center Front (0, 1.0, z)
```
         +Y
          ↑
          |
       [Drone]  ← Facing: BACKWARD (toward performer)
       ↓ camera
          |
       Performer
       (0, 0)
```
- **Position**: 1 meter in front of performer
- **Facing**: Toward negative Y (180°)
- **Camera points at**: Performer's face

### 2. Right Side (1.0, 1.0, z)
```
         +Y
          ↑
          |
       [Drone]
       ↙ camera
          |
       Performer
       (0, 0)
```
- **Position**: 1 meter right and 1 meter front
- **Facing**: Diagonal toward performer (~225°)
- **Camera points at**: Performer from side angle

### 3. Left Side (-1.0, 1.0, z)
```
         +Y
          ↑
          |
       [Drone]
       ↘ camera
          |
       Performer
       (0, 0)
```
- **Position**: 1 meter left and 1 meter front
- **Facing**: Diagonal toward performer (~135°)
- **Camera points at**: Performer from side angle

### 4. Retreat Position (0, -0.5, z)
```
         +Y
          ↑
          |
       Performer
       (0, 0)
          ↑
       camera
       [Drone]
          |
```
- **Position**: 0.5 meters behind performer
- **Facing**: Toward positive Y (0°)
- **Camera points at**: Performer from behind

## How It Works

### Face Center Calculation
The `face_center_yaw_deg()` function calculates the yaw angle needed to face the performer:

```python
def face_center_yaw_deg(px, py, cx, cy, world_yaw_offset_deg=0.0):
    ang = math.degrees(math.atan2(cy - py, cx - px))
    return ang + world_yaw_offset_deg
```

Where:
- `(px, py)` = Drone's current position
- `(cx, cy)` = Performer's position (0, 0)
- `world_yaw_offset_deg` = Additional rotation offset

### Example Calculations

**Center Front (0, 1.0)**:
```python
atan2(0 - 1.0, 0 - 0) = atan2(-1, 0) = -90° = 270° = facing negative Y ✓
```

**Right Side (1.0, 1.0)**:
```python
atan2(0 - 1.0, 0 - 1.0) = atan2(-1, -1) = -135° = 225° = facing diagonal ✓
```

**Retreat (0, -0.5)**:
```python
atan2(0 - (-0.5), 0 - 0) = atan2(0.5, 0) = 90° = facing positive Y ✓
```

## Movement Behavior

### Linear Movements (goto function)
When moving from point A to point B:
1. Drone calculates yaw to face performer at destination
2. Rotates to correct orientation during movement
3. Arrives facing performer

### Circular Movements (circle, spiral, wave)
During orbits:
1. Each segment calculates yaw to face center (performer)
2. Drone continuously adjusts orientation
3. Always facing inward toward performer

## Troubleshooting

### Problem: Drone flies behind performer
**Cause**: Not calculating yaw correctly
**Solution**: ✅ Fixed! Now uses `face_center_yaw_deg()` in `goto()`

### Problem: Drone faces wrong direction
**Check**:
1. Performer position set to (0, 0)? ✓
2. `face_performer=True` in goto calls? ✓
3. `FACE_CENTER=True` in circle/spiral? ✓

### Problem: Drone spins during movement
**Cause**: Yaw changing too rapidly
**Solution**: Increase movement duration for smoother rotation

## Safety Considerations

### Always Facing Performer Benefits:
1. **Camera framing**: Performer always in shot
2. **Predictable behavior**: Easier to anticipate movements
3. **Safety awareness**: Front sensors (if any) face performer
4. **Visual aesthetics**: More intentional choreography

### Front of Drone Orientation:
- **Forward (X+)** = Drone's nose/camera direction in body frame
- **When facing performer**: Drone's X+ axis points toward (0, 0)
- **Props**: Should never point directly at performer (maintain distance)

## Testing Orientation

### Visual Check:
1. Place drone at center front (0, 1.0, 1.5)
2. Drone should face backward toward performer
3. Camera LED (if any) should point at performer

### Movement Check:
1. Fly to right side (1.0, 1.0, 1.5)
2. Drone should rotate to face performer (diagonal)
3. Front still points toward performer

### Circle Check:
1. Start circle movement
2. Drone should rotate continuously
3. Front always points toward center (performer)

## Configuration

### Enable/Disable Face Performer:
```python
# In goto() calls - can be controlled per movement
goto(hl, POINTS["CENTER"], H_STD, 5.0, face_performer=True)   # Faces performer
goto(hl, POINTS["CENTER"], H_STD, 5.0, face_performer=False)  # No rotation
```

### Adjust Yaw Offset:
```python
# Global offset for all movements
YAW_OFF_DEG = 0.0    # No offset (default)
YAW_OFF_DEG = 90.0   # Rotate 90° clockwise from facing performer
YAW_OFF_DEG = -90.0  # Rotate 90° counter-clockwise
```

## Expected Behavior Summary

| Position | Yaw Angle | Facing Direction | Camera View |
|----------|-----------|------------------|-------------|
| Center Front (0, 1.0) | ~270° | ← Backward | Full frontal |
| Right Side (1.0, 1.0) | ~225° | ↙ Diagonal | Right profile |
| Left Side (-1.0, 1.0) | ~135° | ↘ Diagonal | Left profile |
| Retreat (0, -0.5) | ~90° | ↑ Forward | Back of head |
| During Circle | Continuous | ← Always inward | Orbiting view |

With this fix, the drone should now maintain proper orientation and not fly behind the performer unexpectedly! 🚁✨
