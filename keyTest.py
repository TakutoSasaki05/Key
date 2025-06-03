import requests
import gpiozero
import time
# PIN_number
sensorPin = 3
ledPin = 5

# GPIO
sensorInput = gpiozero.DigitalInputDevice(sensorPin)
ledOutput = gpiozero.DigitalOutputDevice(ledPin)

def system():
    last_state = False
    
    try:
        while True:
            now_state = sensor()
            if now_state != last_state:
                led(now_state)
                slack(now_state)
                last_state = now_state
            time.sleep(0.5)
    finally:
        ledOutput.off()

def sensor():
    print(sensorInput.value)#test
    return sensorInput.value

def led(i):
    if i:
        ledOutput.off()
    else :
        ledOutput.on()

def slack(i):
    URL = 'https://hooks.slack.com/services/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'
    if i:    
        message = {
            "text": "no_key"
        }
    else :
        message = {
            "text": "key_hear"
        }

    requests.post(URL,json=message)


system()