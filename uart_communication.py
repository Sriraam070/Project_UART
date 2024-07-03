import serial

# Initialize the serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your actual serial port

def send_command(command):
    ser.write(command.encode('utf-8'))

def receive_response():
    while ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(f"Received: {response}")
        return response

if __name__ == "__main__":
    while True:
        command = input("Enter command to send: ")
        send_command(command)
        receive_response()
