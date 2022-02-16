import paho.mqtt.client as mqtt
import os
import logging
logging.basicConfig()
import mppsolar
# import mppsolar.mpp_info_pub;
from mppsolar.mpputils import mppUtils

# mppsolar.mpp_info_pub.main()
    
def on_connect(a,b,c,d):
    print("CONNECTED!!!")
    
def on_message(client, userdata, message):
    print("Received command '" + str(message.payload) + "'")
    res = mp.getResponse(str(message.payload))
    print("Response: " + res)
    client.publish(os.environ['MQTT_RES_TOPIC'], res, 0, False)

def main():
    # print(os.environ)
    print("Starting...")
    global client
    global mp
    client = mqtt.Client(client_id=os.environ['MQTT_CLIENT_ID'])
    client.username_pw_set(os.environ['MQTT_USER'], os.environ['MQTT_PASS'])
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    # client.loop_start()
    client.subscribe(os.environ['MQTT_TOPIC'])
    
    mp = mppUtils('/dev/hidraw0', 2400)
    
    client.loop_forever()
    # try:
    #     global file
    #     global fd
    #     file = open('/dev/hidraw0', 'r+')
    #     fd = file.fileno()
    #     fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    #     fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    # except Exception as e:
    #     print('error open file descriptor: ' + str(e))
    #     exit()

if __name__ == '__main__':
    main()
