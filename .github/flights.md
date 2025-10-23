
🛩️ MR Drone Routines — Deeproot Hand-off

Song: Incomple🧭 Performance Space

Region	Description
Center Front	1 meter in front of performer at (0, 1.0, z) — main hover zone
Retreat Zone	~1.5 m backward from center front at (0, -0.5, z)
Left / Right Zones	±1 m lateral offset from center at (±1.0, 1.0, z)
Height Range	1.2 m (low) – 2.0 m (high), standard hover at 1.5 m
Safety Zone	Drone remains outside performer's immediate area during orbits
Circle Orbit	0.8 m radius around performer at origin (0, 0, z)

All coordinates assume the performer is at origin (0, 0). The drone starts on the ground at center front (0, 1.0, 0), takes off vertically, and performs movements relative to this coordinate system.

⸻tps://www.youtube.com/watch?v=t1ast4AFKp4

This repository contains modular flight routine scripts for the MR Drone project — including reusable motion primitives (forward, circle, diag, etc.) and a complete choreographed performance that synchronizes with the music "Incomplete".
The drone's movements are designed to express emotion and spatial flow around a human performer while maintaining safe boundaries.

⸻

📍 Coordinate System & Initial Setup

**Performer Position**: Origin (0, 0, 0)
**Center Front**: 1 meter in front of performer at (0, 1.0, 0)
- This is where the drone starts and returns to throughout the performance
- Positive Y points toward audience (away from performer)
- Positive X points to performer's right
- Positive Z points upward

**Initial Drone Placement**: Place drone on ground at center front position (0, 1.0, 0), facing the performer (toward negative Y direction).

⸻rone Routines — Deeproot Hand-off

Song: Incomplete 

This repository contains modular flight routine scripts for the MR Drone project — including reusable motion primitives (forward, circle, diag, etc.) and a complete choreographed performance that synchronizes with the music “Incomplete”.
The drone’s movements are designed to express emotion and spatial flow around a human performer while maintaining safe boundaries.

⸻

📂 Directory Contents

backward.py
circle.py
curves.py
diag.py
downward.py
figure8.py
forward.py
hover.py
land.py
left.py
slowing_circles.py

takeoff.py
spiral.py
cfutils.py
main.py

✅ Fixes & Additions
	•	Fixed cfutils.hl_move_distance_compat variable mismatch (y typo).
	•	Added takeoff.py and spiral.py for modular completeness.
	•	Updated main routine to follow “Incomplete” musical timing.
	•	Added structured hover, approach, retreat, diagonal, and spiral motions.

⸻

🧭 Performance Space

Region	Description
Center Front	Main hover zone directly in front of dancer
Retreat Zone	~1.5 m backward from center
Left / Right Zones	±1 m lateral offset from center
Height Range	1.2 m (low) – 2.0 m (high)
Safety Zone	Drone remains outside performer’s 1×1 m safety box

All coordinates assume the origin (0,0) is the performer’s center point. The drone starts and ends at center front, facing the performer.

⸻

🎶 Choreography Timeline (Synced with “Incomplete”)

Pre-Dance (Takeoff + Intro, 0:00–0:15)

Time	Action	Description
Takeoff	—	Drone ascends vertically from ground to 1.5 m height at center front (0, 1.0, 1.5).
0:00–0:05	Hover	Maintain position at center front at 1.5 m height.
0:05–0:10	Retreat	Move backward to (0, -0.5, 1.5) — approximately 1.5 m away from center front.
0:10–0:15	Approach	Return smoothly to center front (0, 1.0, 1.5).

⸻

Main Dance Routine (0:16–3:30)

🟩 Directional Movement and Circle Phase

Time	Action	Description
0:16–0:20	Fly right	Move to (1.0, 1.0, 1.5) — 1 m to the right of center front.
0:21–0:23	Hover	Hold position at right side.
0:23–0:29	Fly center	Return to center front (0, 1.0, 1.5).
0:30–0:36	Fly left	Move to (-1.0, 1.0, 1.5) — 1 m to the left of center front.
0:37–0:40	Hover	Hold position at left side.
0:40–0:46	Fly center	Return to center front (0, 1.0, 1.5).
0:46–1:15	Circle	Circle around the performer at 0.8 m radius (flat, counterclockwise), maintain 1.5 m height. Circle center is at performer position (0, 0, 1.5). End back at center front.

🟦 Approach / Retreat & Diagonal Phase

Time	Action	Description
1:16–1:20	Retreat	Move backward to (0, -0.5, 1.5).
1:21–1:26	Approach	Return to center front (0, 1.0, 1.5).
1:26–1:50	Diagonal sweeps	Alternate upward and downward diagonal motions (8 passes total, 3 seconds each).
—	—	• Each diagonal: move 1.5 m horizontal distance while changing 1.2 m in height.
—	—	• Movements orbit around performer while alternating up/down.
—	—	• Pass 1 (up): 1.2 m → 2.4 m height
—	—	• Pass 2 (down): 2.4 m → 1.2 m height
—	—	• Continues alternating for 8 total passes.

🌀 Spiral and Orbit Phase

Time	Action	Description
1:50–2:20	Spiral flight	Spiral upward around the performer (0.8 m radius orbit). Height transitions from 1.5 m → 2.0 m. Ends at center front.

🟥 Diagonal Approach / Retreat Phase

Time	Action	Description
2:21–2:25	Retreat	Move to (0, -0.5, 1.5).
2:25–2:28	Hover	Pause at retreat position.
2:28–2:32	Approach	Move to center front (0, 1.0, 1.5).
2:32–2:36	Retreat	Move to (0, -0.5, 1.5) again.
2:36–2:39	Hover	Hold position at retreat.
2:39–2:43	Approach	Move to center front (0, 1.0, 1.5) again.

🔵 3D Expression Phase

Time	Action	Description
2:43–2:51	Draw sphere	Trace a spherical (or circular vertical) path at center front, 0.35 m radius around (0, 1.0, 1.5).
2:51–3:30	Wave orbit	Smooth, slow wave-like motion circling the performer (0.8 m radius). Gradual deceleration toward ending. Height oscillates between 1.5 m – 2.0 m. Ends at center front.


⸻

Post-Dance (3:30–3:43)

Time	Action	Description
3:30–3:35	Retreat	Slow backward movement to (0, -0.5, 1.5).
3:35–3:43	Approach	Return to center front (0, 1.0, 1.5) for the closing pose.
3:43+	Descent	Smooth vertical landing at center front position.


⸻

⚙️ Parameter Summary

Variable	Default	Description
CHEST_Z	1.5 m	Standard hover altitude
HIGH_Z	2.0 m	Spiral & wave max height
LOW_Z	1.2 m	Diagonal phase base height
CENTER_FRONT_Y	1.0 m	Y-coordinate of center front (in front of performer)
RETREAT_DIST	1.5 m	Distance backward from center front
SIDE_DIST	1.0 m	Left/right offset from center line
DIAG_HORIZONTAL	1.5 m	Horizontal distance per diagonal pass
DIAG_VERTICAL	1.2 m	Height change per diagonal pass
ASCENT_VEL	0.7 m/s	Takeoff velocity
DESCENT_VEL	0.25 m/s	Landing velocity
CIRCLE_R	0.8 m	Circle radius around performer
FACE_CENTER	True	Always face performer during orbits


⸻

🧩 Modular Motion Components

File	Purpose
forward/backward/left/diag	Basic relative motions
circle.py	Circular path with yaw control
spiral.py	Ascending/descending orbital spiral
curves.py, slowing_circles.py	Smooth arcs and tempo variations
figure8.py	Decorative rhythmic pattern
hover.py, land.py, takeoff.py	Vertical control primitives
cfutils.py	Robust Crazyflie HL API wrapper
main.py	Complete timeline routine for “Incomplete”


⸻

🧠 Behavior Logic
	•	Each movement includes a time buffer (+0.05 s) to ensure stable transitions.
	•	Absolute paths use go_to; relative paths use move_distance.
	•	No command overlaps; every routine step completes before next execution.
	•	Failsafe stop + disarm triggers upon KeyboardInterrupt or unexpected disconnection.

⸻

🪫 Fail-safe Procedure

In case of manual abort:
	1.	Ctrl + C immediately halts the sequence.
	2.	Drone issues cf.high_level_commander.stop().
	3.	System sends cf.platform.send_arming_request(False) to disarm.

⸻

🧾 License

Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0)
© 2025 MR Drone Project — De La Salle University Manila

⸻

Would you like me to update your main.py choreography code next so it actually performs this new Incomplete timeline (hover, approach, circle, diagonals, spiral, wave, etc.) in sequence using your current flight helper modules (hl_move_distance_compat, circle, spiral_arc, etc.)?
That would give you a ready-to-fly Python script synced to this updated design.