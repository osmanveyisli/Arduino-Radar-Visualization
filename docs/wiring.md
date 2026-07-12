# Wiring Guide

## HC-SR04 Ultrasonic Sensor

| HC-SR04 Pin | Arduino Pin |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | 6 |
| ECHO | 7 |

## ULN2003 Stepper Motor Driver

| ULN2003 Pin | Arduino Pin |
|---|---|
| IN1 | 8 |
| IN2 | 9 |
| IN3 | 10 |
| IN4 | 11 |
| VCC | 5V |
| GND | GND |

The 28BYJ-48 stepper motor connects directly to the ULN2003 driver board.

## Important Notes

- Position the ultrasonic sensor manually at the 0° starting angle before powering the system.
- Ensure the Arduino and ULN2003 driver share a common ground.
- If the stepper motor behaves erratically, use a separate 5V power supply for the motor driver while keeping the grounds connected.
