# Voice-Controlled Healthcare Robot Using Arduino and UART Algorithm

## Project Overview
This project focuses on developing a voice-controlled healthcare robot using Arduino. The robot leverages advanced UART algorithms to optimize communication efficiency and interact seamlessly in healthcare environments to enhance patient care delivery.

## Components
- Arduino Uno
- Elechouse Voice Recognition Module V3
- UART Module
- L298N Motor Driver
- Ultrasonic Sensor
- Temperature Sensor
- Chassis and Wheels
- Power Supply (Battery Pack)
- Jumper Wires, Breadboard, Resistors

## Setup and Usage
1. **Voice Recognition Module:**
   - Connect the voice recognition module to Arduino.
   - Train the module with specific voice commands (e.g., "Forward," "Backward," "Left," "Right," "Stop").

2. **Motor Control:**
   - Connect the motors to the L298N motor driver and Arduino.

3. **UART Communication:**
   - Set up UART communication between the Arduino and the voice recognition module.

4. **Run the Code:**
   - Upload the provided code to the Arduino.
   - Ensure the power supply is connected and the robot is placed on a flat surface.
   - Use voice commands to control the robot.

## Files
- `voice_control.py`: Main code for voice recognition and motor control.
- `uart_communication.py`: Code for UART communication.
- `motor_control.py`: Code for controlling the motors.
- `README.md`: Project documentation.

## Future Enhancements
- Integrate additional sensors (e.g., obstacle detection, temperature monitoring).
- Improve voice command recognition accuracy.
- Add more sophisticated movements and commands.
