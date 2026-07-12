# System Architecture

```mermaid
flowchart LR
    A[HC-SR04 Ultrasonic Sensor] --> B[Arduino Uno]
    C[28BYJ-48 Stepper Motor] <--> D[ULN2003 Motor Driver]
    D <--> B
    B -->|Angle, Distance via Serial| E[Python Application]
    E --> F[Pygame Radar Visualization]
