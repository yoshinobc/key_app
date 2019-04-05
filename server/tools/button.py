import RPi.GPIO as GPIO
import time

def lock():
    GPIO.setmode(GPIO.BCM) #チップ依存のGPIOピン名称をチャンネルとして扱う

    gp_out = 4
    GPIO.setup(gp_out,GPIO.OUT) #setup(チャンネル,GPIO.OUT) チャンネル4を出力モード
    servo = GPIO.PWM(gp_out,50)
    servo.start(0) #デューティ比0
    servo.ChamgeDutyCycle(2.5) #デューティ比を変更
    time.sleep(0.5)
    servo.stop()
    GPIO.cleanup()

def unlock():
    GPIO.setmode(GPIO.BCM) #チップ依存のGPIOピン名称をチャンネルとして扱う

    gp_out = 4
    GPIO.setup(gp_out,GPIO.OUT) #setup(チャンネル,GPIO.OUT) チャンネル4を出力モード
    servo = GPIO.PWM(gp_out,50)
    servo.start(0) #デューティ比0
    servo.ChamgeDutyCycle(12) #デューティ比を変更
    time.sleep(0.5)
    servo.stop()
    GPIO.cleanup()
