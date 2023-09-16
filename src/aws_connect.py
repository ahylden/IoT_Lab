import time
import paho.mqtt.client as mqtt
import ssl
import json
import _thread

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='../certs/rootCA.pem', certfile='../certs/certificate.pem.crt', keyfile='../certs/private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a3vqslwjgydv4a-ats.iot.us-east-2.amazonaws.com", 8883, 60)

def publishData(txt):
    print(txt)
    client.publish("$aws/things/RaspberryPi/shadow/name/raspi", payload=json.dumps({"msg": txt}), qos=0, retain=False)
        
#_thread.start_new_thread(publishData,("Spin-up new Thread...",))

#client.loop_forever()