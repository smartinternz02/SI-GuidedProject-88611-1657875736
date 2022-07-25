#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "ct0pun",
        "typeId": "nodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    vol=random.randint(0,100)
    cur=random.randint(0,100)
    tim=24
    unit=5
    p=vol*cur
    energy=p*tim
    bill=energy*unit
    myData={'Voltage':vol,'Current':cur,'Electricity_bill':bill}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully:", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
