import serial
import time

# Set up the serial communication
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your actual serial port

def move_forward():
    print("Moving Forward")
    # Add motor control code here
    ser.write(b'F')

def move_backward():
    print("Moving Backward")
    # Add motor control code here
    ser.write(b'B')

def turn_left():
    print("Turning Left")
    # Add motor control code here
    ser.write(b'L')

def turn_right():
    print("Turning Right")
    # Add motor control code here
    ser.write(b'R')

def stop_moving():
    print("Stopping")
    # Add motor control code here
    ser.write(b'S')

def listen_for_commands():
    while True:
        if ser.in_waiting > 0:
            command = ser.readline().decode('utf-8').strip()
            if command == "Forward":
                move_forward()
            elif command == "Backward":
                move_backward()
            elif command == "Left":
                turn_left()
            elif command == "Right":
                turn_right()
            elif command == "Stop":
                stop_moving()
            else:
                print(f"Unknown command: {command}")

if __name__ == "__main__":
    listen_for_commands()
