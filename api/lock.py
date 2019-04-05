import falcon

class lock(object):

    def on_post(self,req,resp):
        import RPi.GPIO as GPIO

        resp.status = falcon.HTTP_400
        GPIO.setmode(GPIO.BCM) #チップ依存のGPIOピン名称をチャンネルとして扱う

        gp_out = 4
        GPIO.setup(gp_out,GPIO.OUT) #setup(チャンネル,GPIO.OUT) チャンネル4を出力モード

        servo = GPIO.PWM(gp_out,50)

        servo.start(0) #デューティ比0

        servo.ChamgeDutyCycle(2.5) #デューティ比を変更
        resp.status = falcon.HTTP_200
        servo.stop()
        GPIO.cleanup()
        resp.body = '{"message":locked}'

        return resp
