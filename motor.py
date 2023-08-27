import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class motors():
    def __init__(self, Ena1, In1, In2,Ena2, In3, In4):
        self.Ena1 = Ena1
        self.In1 = In1
        self.In2 = In2
        self.Ena2 = Ena2
        self.In3 = In3
        self.In4 = In4

        GPIO.setup(self.Ena1, GPIO.OUT)
        GPIO.setup(self.Ena2, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
        GPIO.setup(self.In3, GPIO.OUT)
        GPIO.setup(self.In4, GPIO.OUT)
        self.pwm1 = GPIO.PWM(self.Ena1, 100)
        self.pwm2 = GPIO.PWM(self.Ena2, 100)

        self.pwm1.start(0)
        self.pwm2.start(0)

    def moveF(self,x):
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(x)

        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        #sleep(t)

    def left(self, x,y):
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(y)
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        #sleep(t)

    def right(self, x,y):
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(y)
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        #sleep(t)



    def moveB(self, x):
        self.pwm1.ChangeDutyCycle(x)
        self.pwm2.ChangeDutyCycle(x)
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)


    def stop(self, t=2):
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)
        sleep(t)

#motor1 = motors(2, 3, 4,17,22,27)

'''while True:
    motor1.moveF(30, 2)
    motor1.stop(1)
    motor1.moveB(50,2)
    motor1.stop(1)
    motor1.right(50,30,2)
    motor1.stop(1)
    motor1.left(30,50,2)'''




