# Circle and Spiral Pattern Fixes

## Issue 1: Circle Starting Point - FIXED ✅

### Problem:
The circle was starting at `(0.8, 0, 1.5)` (to the right of performer) instead of at center front `(0, 1.0, 1.5)`.

### Solution:
Added `start_angle_deg` parameter to the `circle()` function.

### Mathematical Explanation:

For a circle centered at `(cx, cy)` with radius `r`:
- `x = cx + r * cos(θ)`
- `y = cy + r * sin(θ)`

To start at center front `(0, 1.0)`:
- We need: `0 = 0 + 0.8 * cos(θ)` → `cos(θ) = 0`
- And: `1.0 = 0 + 0.8 * sin(θ)` → `sin(θ) = 1.25`

Wait, that doesn't work because radius is 0.8m but center front is 1.0m from origin!

### The Real Issue:
The **radius (0.8m) is less than the distance to center front (1.0m)**!

Center front is at distance: `√(0² + 1.0²) = 1.0m` from performer
Circle radius is: `0.8m`

**Center front is OUTSIDE the circle orbit!** 🎯

### Two Solutions:

#### Option A: Increase Circle Radius to 1.0m
```python
CIRCLE_R = 1.0  # Match distance to center front
```

Then start at 90°:
- `x = 0 + 1.0 * cos(90°) = 0` ✓
- `y = 0 + 1.0 * sin(90°) = 1.0` ✓

#### Option B: Keep 0.8m radius, start from closest point
The circle at 0.8m radius comes closest to center front at angle 90°:
- Point: `(0, 0.8, 1.5)` - 0.8m in front of performer
- Then move to center front before/after circle

### Current Implementation (Option B):
```python
# Before circle: drone is at center front (0, 1.0)
# Move to circle starting point (0, 0.8) 
goto(hl, (0, 0.8), H_STD, 0.5)

# Circle at 0.8m radius starting from top (90°)
circle(hl, cx=0.0, cy=0.0, radius=0.8, start_angle_deg=90.0)

# Return to center front after circle
goto(hl, POINTS["CENTER"], H_STD, 0.6)
```

## Issue 2: Spiral Pattern - FIXED ✅

### Problem:
Original `spiral_arc()` created a **vertical spiral** (orbiting while ascending), but you wanted **horizontal overlapping circles** in front of the dancer.

### Solution:
Created new `horizontal_figure8()` function that draws a lemniscate (∞ shape) pattern.

### Pattern Visualization:

```
         Dancer at (0, 0)
              ●
              
        ╱───────╲
       ╱    ●    ╲    ← Center front (0, 1.0)
      │  ╱     ╲  │
      │ │   🚁  │ │   ← Figure-8 path
      │  ╲     ╱  │
       ╲    ●    ╱
        ╲───────╱
        
    Overlapping circles
    creating figure-8
```

### Mathematical Pattern:

The horizontal figure-8 uses a lemniscate curve:

```python
# Parametric equations (0 ≤ t ≤ 2π)
px = cx + (width/2) * sin(t) * cos(t) / (1 + 0.3*sin²(t))
py = cy + (width/3) * cos(t)
pz = z + height_var * sin(2t)  # Slight vertical wave
```

This creates:
- **Horizontal twisting motion** (left-right oscillation)
- **Overlapping circles** in the X-Y plane
- **Slight height variation** for visual interest
- **Always facing performer** at (0, 0)

### Parameters:
- `width=1.2`: Left-right extent of the pattern
- `height_var=0.3`: Vertical oscillation amplitude
- `total_time=30.0`: Duration (1:50-2:20 = 30 seconds)
- `segments=60`: Smooth path with 60 waypoints

## Visual Comparison

### Before (Vertical Spiral):
```
Side View:
    2.0m ──●────●─── ← Top of spiral
         ╱│     │╲
    1.8m● │  🚁│ ●
       ╱  │     │  ╲
    1.6m  │     │   ●
         ╱      │    
    1.5m●───────●─── ← Start
    
    (Ascending while orbiting)
```

### After (Horizontal Figure-8):
```
Top View:
           ┌─────┐
           │  ●  │ ← Dancer
           └──┬──┘
              │
         ╭────●────╮
        ╱  ╱   ╲  ╲
       │  ╱  🚁 ╲  │
       │ ╱       ╲ │
        ╲╱       ╲╱
         ●       ●
         
    (Horizontal twisting motion)
```

## Updated Code Files

### 1. `circle.py` - Added start_angle_deg parameter
```python
def circle(..., start_angle_deg=0.0):
    start_angle_rad = math.radians(start_angle_deg)
    for k in range(segments + 1):
        theta = start_angle_rad + 2.0 * pi * (k / segments)
        # ... rest of circle code
```

### 2. `figure8_horizontal.py` - New file
```python
def horizontal_figure8(hl, *, cx, cy, z, width, height_var, ...):
    # Creates horizontal figure-8 pattern
    # Overlapping circles in front of dancer
```

### 3. `main.py` - Updated calls
```python
# Circle with proper starting position
circle(hl, cx=0.0, cy=0.0, radius=0.8,
       start_angle_deg=90.0)  # Start from top

# Horizontal figure-8 instead of vertical spiral
horizontal_figure8(hl, cx=0.0, cy=1.0,
                   width=1.2, height_var=0.3)
```

## Choreography Timeline Updates

### 0:46–1:15 Circle Movement
- **Start**: Center front (0, 1.0, 1.5)
- **Pattern**: Orbit around performer (0, 0) at 0.8m radius
- **Starting angle**: 90° (top of circle, closest to center front)
- **End**: Returns to starting point, then moves to center front

### 1:50–2:20 Horizontal Figure-8
- **Start**: Center front (0, 1.0, 1.5)
- **Pattern**: Horizontal figure-8 with overlapping circles
- **Width**: 1.2m (left-right extent)
- **Height variation**: ±0.3m for visual interest
- **End**: Returns to center front

## Testing Recommendations

1. **Test circle starting point**:
   - Verify drone starts from near center front
   - Check if radius needs adjustment to 1.0m
   - Confirm smooth transition into orbit

2. **Test horizontal figure-8**:
   - Observe the overlapping circle pattern
   - Adjust `width` parameter if too wide/narrow
   - Tune `height_var` for desired vertical motion
   - Check that pattern stays in front of dancer

3. **Visual verification**:
   - Drone should always face performer
   - Movements should feel intentional, not random
   - Patterns should be smooth and continuous

## Alternative Configurations

### Tighter Figure-8:
```python
horizontal_figure8(hl, width=0.8, height_var=0.2)
```

### Wider, More Dynamic:
```python
horizontal_figure8(hl, width=1.6, height_var=0.5)
```

### Flat (No Height Variation):
```python
horizontal_figure8(hl, width=1.2, height_var=0.0)
```

## Notes

- Both patterns now maintain proper orientation (facing performer)
- Circle orbit is around performer at (0, 0)
- Figure-8 is centered at center front (0, 1.0) for visibility
- All movements include keyboard interrupt monitoring
- UDP streaming continues throughout all patterns
