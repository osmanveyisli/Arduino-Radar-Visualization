# Arduino Radar Visualization

A real-time embedded sensing system that combines ultrasonic distance measurement, stepper motor scanning, and Python-based visualization for environmental scanning and obstacle detection.

## Overview

This project uses an Arduino Uno, an HC-SR04 ultrasonic sensor, and a 28BYJ-48 stepper motor to scan an area across 180 degrees. The Arduino transmits angle and distance measurements through serial communication to a Python application, which displays the detected objects in real time using Pygame.

The project demonstrates embedded programming, sensor integration, motor control, serial communication, coordinate transformation, and real-time data visualization.

## Features

- Real-time ultrasonic distance measurement
- 180-degree rotational scanning
- Stepper motor control through a ULN2003 driver
- Serial communication between Arduino and Python
- Live radar-style visualization using Pygame
- Polar-to-Cartesian coordinate conversion
- Persistent obstacle plotting by scanning angle

## Hardware

- Arduino Uno
- HC-SR04 ultrasonic sensor
- 28BYJ-48 stepper motor
- ULN2003 motor driver
- Breadboard
- Jumper wires
- USB cable

## Software

- Arduino C++
- Python
- Pygame
- PySerial

## Repository Structure

```text
Arduino-Radar-Visualization/
├── README.md
├── requirements.txt
├── .gitignore
├── arduino/
│   └── radar_controller.ino
├── python/
│   └── radar_visualizer.py
└── docs/
    ├── system_architecture.md
    └── wiring.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Anormal38/Arduino-Radar-Visualization.git
cd Arduino-Radar-Visualization
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Upload `arduino/radar_controller.ino` to the Arduino Uno using the Arduino IDE.

## Usage

1. Assemble the hardware using the instructions in `docs/wiring.md`.
2. Manually position the ultrasonic sensor at the starting angle.
3. Connect the Arduino to the computer.
4. Change the serial port in `python/radar_visualizer.py` if required:

```python
arduino = serial.Serial("COM7", 9600)
```

5. Run the Python application:

```bash
python python/radar_visualizer.py
```

The Arduino sends measurements in this format:

```text
angle,distance
```

For example:

```text
45,23
46,22
47,24
```

## How It Works

1. The stepper motor rotates the ultrasonic sensor across the scanning range.
2. The HC-SR04 measures the distance at each angle.
3. The Arduino sends the angle and distance to the computer through serial communication.
4. Python converts the polar measurements into Cartesian coordinates.
5. Pygame plots the detected objects on a live radar-style display.

Detailed architecture and wiring information are available in the `docs` folder.

## Limitations

- The sensor must be manually aligned before startup.
- The stepper motor does not provide absolute position feedback.
- Measurement accuracy depends on the shape and angle of detected surfaces.
- Ultrasonic sensor noise is not currently filtered.
- The visualizer stores one measurement for each scanning angle.

## Future Improvements

- Automatic homing using a limit switch
- Sensor noise filtering
- Configurable serial-port selection
- Adjustable visualization scale
- Room-outline reconstruction
- Scan-data export for later analysis
- Integration with an autonomous robotic platform

## License

This project is licensed under the MIT License.  
