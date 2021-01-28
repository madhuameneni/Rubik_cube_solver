import RPi.GPIO as GPIO
import time

# GPIO [14, 15, 18, 23]
# U  -> 0001
# U' -> 0010
# F  -> 0011
# F' -> 0100
# D  -> 0101
# D' -> 0110
# L  -> 0111
# L' -> 1000
# R  -> 1001
# R' -> 1010
# B  -> 1011
# B' -> 1100


class Rotating:

    def rotating(self, final_data):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        for i in final_data:
            if i == "U":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "U'":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            elif i == "F":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "F'":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.HIGH)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            elif i == "D":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.HIGH)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "D'":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.HIGH)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            elif i == "L":
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.HIGH)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "L'":
                GPIO.setup(14, GPIO.HIGH)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            elif i == "R":
                GPIO.setup(14, GPIO.HIGH)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "R'":
                GPIO.setup(14, GPIO.HIGH)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            elif i == "B":
                GPIO.setup(14, GPIO.HIGH)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.HIGH)
                GPIO.setup(23, GPIO.HIGH)
                time.sleep(10)
            elif i == "B'":
                GPIO.setup(14, GPIO.HIGH)
                GPIO.setup(15, GPIO.HIGH)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.LOW)
                time.sleep(10)
            else:
                GPIO.setup(14, GPIO.LOW)
                GPIO.setup(15, GPIO.LOW)
                GPIO.setup(18, GPIO.LOW)
                GPIO.setup(23, GPIO.LOW)

        print("Rubik Cibe is solved by our Team")
        return True

