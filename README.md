# Real-Time Embedded Radar System

A real-time embedded radar platform that combines ultrasonic sensing, stepper motor scanning, and Python-based visualization to perform rotational environmental scanning and obstacle detection.

## Overview

This project implements an embedded radar system using an Arduino, an HC-SR04 ultrasonic sensor, and a 28BYJ-48 stepper motor. Distance measurements are transmitted over serial communication to a Python application, where they are visualized in real time as a radar display.

The system demonstrates the integration of embedded hardware, serial communication, and desktop visualization to create an interactive environmental sensing platform.

## Features

- Real-time ultrasonic distance measurement
- 180° rotational scanning using a stepper motor
- Serial communication between Arduino and Python
- Live radar-style visualization using Pygame
- Polar-to-Cartesian coordinate conversion
- Persistent obstacle plotting by scan angle

## System Architecture

The HC-SR04 ultrasonic sensor is rotated by a 28BYJ-48 stepper motor controlled through a ULN2003 driver. The Arduino collects angle and distance measurements and transmits them to a Python application over serial communication. The Python program converts polar measurements into Cartesian coordinates and renders them in real time using Pygame.

## Hardware

- Arduino Uno
- HC-SR04 ultrasonic sensor
- 28BYJ-48 stepper motor
- ULN2003 motor driver
- Breadboard and jumper wires

- ## Software

- Arduino C++
- Python
- Pygame
- PySerial
