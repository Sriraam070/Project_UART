import RPi.GPIO as GPIO
import time

# Define GPIO pins
motor1_pin1 = 17
motor1_pin2 = 18
motor2_pin1 = 22
motor2_pin2 = 23

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

def move_forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def move_backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

def turn_left():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def turn_right():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

def stop_moving():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            command = input("Enter command (w/s/a/d/stop): ")
            if command == 'w':
                move_forward()
            elif command == 's':
                move_backward()
            elif command == 'a':
                turn_left()
            elif command == 'd':
                turn_right()
            elif command == 'stop':
                stop_moving()
            else:
                print("Invalid command")
    except KeyboardInterrupt:
        GPIO.cleanup()
