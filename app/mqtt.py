import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt_broker_address", 1883, 60)
