from flask import Flask,request
from time import sleep
import RPi.GPIO as GPIO
import pigpio
pi = pigpio.pi()
app = Flask(__name__)
@app.route("/")
def index():
    return "App Works!"
#GPIO pin 20 for sevro
#GPIO pin 26 for pump
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(26,GPIO.OUT,initial=0)
GPIO.setup(21,GPIO.OUT,initial=0)
GPIO.output(21,GPIO.LOW)
@app.route('/power', methods=['POST'])
def onandoff():
    value = request.form.get('value')
    if value=="ON" :
        GPIO.output(26, GPIO.HIGH)
        sleep(1)
    else:
        GPIO.output(26,GPIO.LOW)
    print(value)
    return "got it"
@app.route('/angle', methods=['POST'])
def anglesetter():
    value = int(request.form.get('value'))
    v =  11*value
    pi.set_servo_pulsewidth(20, v+500)
    sleep(1)
    return "got it"
if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True, port=4001)
