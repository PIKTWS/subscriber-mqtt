import paho.mqtt.client as mqtt
# from database import add_mqtt_message 
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+(msg.payload).decode("utf-8"))
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    try:
        payload = json.loads(payload.replace("\'", "\""))
        print(payload)
        with open('data.json', 'a') as f:
            json.dump(payload, f)
            f.write('\n')
    except Exception as e:
        print(e)

    # add_mqtt_message(topic, payload)

client = mqtt.Client()
client.username_pw_set("intern2022", "intern2022")
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.cui.chat", 1883)

client.subscribe("e775b1245d94ea4a79be6ce40cf96929")
client.loop_forever()