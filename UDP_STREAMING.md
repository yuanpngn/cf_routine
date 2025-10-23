# UDP Streaming to Unity

## Overview
The `main.py` script now streams real-time position and orientation data from the Crazyflie drone to your Unity application via UDP, allowing you to visualize the live performance in VR.

## Features

### Real-time Pose Streaming
- **Position**: X, Y, Z coordinates in Crazyflie coordinate system (meters)
- **Orientation**: Yaw angle in degrees
- **Timestamp**: Unix timestamp for synchronization
- **Update Rate**: Configurable (default 30 Hz)

### Packet Format
Same format as `mock_pos.py` for compatibility:
```json
{
  "x": 0.5,
  "y": 0.2,
  "z": 1.5,
  "yaw_deg": 45.0,
  "ts": 1729612345.678
}
```

### Coordinate System
**Crazyflie Coordinates** (sent in packet):
- X: Forward direction
- Y: Left direction
- Z: Up direction

**Unity Mapping** (as per your receiver):
- Unity X = -CF Y (right/left inverted)
- Unity Y = CF Z (height)
- Unity Z = CF X (forward/backward)
- Unity Yaw ≈ -CF Yaw + offset

## Configuration

### Basic Settings
Edit the configuration section at the top of `main.py`:

```python
# UDP Streaming Configuration
UDP_ENABLED = True          # Enable/disable streaming
UDP_IP = "127.0.0.1"        # Destination IP
UDP_PORT = 5005             # Destination port
UDP_HZ = 30.0               # Update rate (Hz)
```

### Common Configurations

#### Local Unity Editor Testing
```python
UDP_ENABLED = True
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
```

#### Quest VR Headset
```python
UDP_ENABLED = True
UDP_IP = "192.168.1.100"    # Your Quest's IP address
UDP_PORT = 5005
```

#### Disable Streaming
```python
UDP_ENABLED = False
```

## How It Works

### 1. Pose Logging Setup
When the drone connects, the system:
- Configures Crazyflie logging for pose data
- Requests position (x, y, z) and yaw from state estimator
- Logs at ~30 Hz (33ms period)

### 2. Background Streaming Thread
- Runs in separate thread (doesn't block choreography)
- Reads latest pose data (thread-safe)
- Sends UDP packets at configured rate
- Continues until performance ends

### 3. Data Flow
```
Crazyflie Drone
    ↓ (Radio link)
pose_callback() ← Logging system
    ↓ (Updates global variable)
latest_pose (thread-safe)
    ↓ (Background thread)
udp_streaming_thread()
    ↓ (UDP packets)
Unity Application
```

## Usage

### Basic Usage
1. **Configure Unity**: Ensure Unity is listening on the correct port
2. **Set IP/Port**: Update `UDP_IP` and `UDP_PORT` in `main.py`
3. **Run Performance**: `python3 main.py`
4. **Monitor**: Check for `[UDP] Streaming started` message

### Output Messages
```
[UDP] Initialized - sending to 127.0.0.1:5005 at 30.0Hz
[ARM] Armed.
[INFO] Press any key at any time to initiate emergency smooth landing...
[UDP] Streaming started
... performance runs ...
[UDP] Streaming stopped
[DISARM] Disarmed.
```

### Testing Without Drone
Use `mock_pos.py` to test Unity visualization:
```bash
python3 mock_pos.py --mode circle --ip 127.0.0.1 --port 5005
```

## Technical Details

### Pose Variables Logged
From Crazyflie firmware:
- `stateEstimate.x` - X position (float, meters)
- `stateEstimate.y` - Y position (float, meters)
- `stateEstimate.z` - Z position (float, meters)
- `stabilizer.yaw` - Yaw angle (float, degrees)

### Thread Safety
- Uses `threading.Lock()` to protect shared data
- `pose_callback()` writes to `latest_pose`
- `udp_streaming_thread()` reads from `latest_pose`
- No race conditions

### Network Protocol
- **Transport**: UDP (User Datagram Protocol)
- **Format**: JSON text
- **Encoding**: UTF-8
- **No acknowledgment**: Fire-and-forget (suitable for real-time streaming)

### Performance Impact
- **Minimal**: Background thread handles streaming
- **Non-blocking**: Doesn't affect choreography timing
- **Configurable rate**: Adjust `UDP_HZ` if needed

## Troubleshooting

### No Data Received in Unity

**Check Network:**
```bash
# Test if port is reachable (on macOS/Linux)
nc -u -l 5005

# Then run main.py - you should see JSON packets
```

**Check IP Address:**
- For Unity Editor: Use `127.0.0.1`
- For Quest: Find Quest IP in settings → WiFi → Connected network
- Ensure both devices on same network

**Check Firewall:**
- macOS: System Preferences → Security & Privacy → Firewall
- Allow Python to accept incoming connections

### Logging Errors

If you see `[UDP] Failed to start logging`:
- Check that Crazyflie firmware supports logging
- Verify variable names match your firmware version
- Try alternative yaw variable: `stateEstimate.yaw` instead of `stabilizer.yaw`

### High Latency

If visualization lags:
- Reduce `UDP_HZ` (e.g., to 20 Hz)
- Check network quality
- Ensure Unity isn't overloaded

### Emergency Landing During Streaming

Streaming continues during emergency landing:
- Position updates reflect emergency descent
- Streaming stops cleanly in `finally` block
- No data corruption

## Comparison: mock_pos.py vs main.py

| Feature | mock_pos.py | main.py |
|---------|-------------|---------|
| Data Source | Simulated patterns | Real Crazyflie drone |
| Position | Calculated (circle, figure8, etc.) | Actual flight data |
| Use Case | Testing Unity without drone | Live performance visualization |
| Packet Format | Identical JSON | Identical JSON |
| Update Rate | Configurable | Configurable |
| Connection | No drone needed | Requires Crazyflie connection |

## Integration with Emergency Landing

UDP streaming is fully integrated with the emergency landing feature:

1. **Press any key** → Triggers emergency landing
2. **Streaming continues** → Unity shows descent
3. **Landing completes** → Streaming stops cleanly
4. **Cleanup** → Socket closed, thread terminated

No data loss or corruption during emergency procedures.

## Advanced Configuration

### Custom Logging Variables

To log additional data, modify `setup_pose_logging()`:

```python
def setup_pose_logging(cf):
    log_conf = LogConfig(name='Pose', period_in_ms=33)
    
    # Standard pose
    log_conf.add_variable('stateEstimate.x', 'float')
    log_conf.add_variable('stateEstimate.y', 'float')
    log_conf.add_variable('stateEstimate.z', 'float')
    log_conf.add_variable('stabilizer.yaw', 'float')
    
    # Add custom variables
    log_conf.add_variable('stabilizer.roll', 'float')
    log_conf.add_variable('stabilizer.pitch', 'float')
    log_conf.add_variable('pm.vbat', 'float')  # Battery voltage
    
    # ... rest of setup
```

Update packet in `pose_callback()`:
```python
latest_pose = {
    "x": data['stateEstimate.x'],
    "y": data['stateEstimate.y'],
    "z": data['stateEstimate.z'],
    "yaw_deg": data['stabilizer.yaw'],
    "roll_deg": data['stabilizer.roll'],
    "pitch_deg": data['stabilizer.pitch'],
    "battery": data['pm.vbat'],
    "ts": time.time()
}
```

### Multiple Receivers

To send to multiple Unity instances:

```python
UDP_DESTINATIONS = [
    ("127.0.0.1", 5005),      # Local editor
    ("192.168.1.100", 5005),  # Quest 1
    ("192.168.1.101", 5005),  # Quest 2
]

# In udp_streaming_thread():
for ip, port in UDP_DESTINATIONS:
    udp_sock.sendto(json.dumps(pkt).encode("utf-8"), (ip, port))
```

## Best Practices

1. **Test with mock_pos.py first** - Verify Unity setup before live flight
2. **Monitor console output** - Watch for UDP errors
3. **Use local IP for testing** - Start with 127.0.0.1
4. **Check network stability** - WiFi quality affects streaming
5. **Keep UDP_HZ reasonable** - 30 Hz is good balance
6. **Enable only when needed** - Set `UDP_ENABLED = False` if not using Unity

## Future Enhancements

Potential improvements:
- Bi-directional communication (Unity → Crazyflie commands)
- Compression for lower bandwidth
- Encryption for secure transmission
- Recording/playback of pose data
- Multiple drone support
- OSC protocol option for creative coding tools
