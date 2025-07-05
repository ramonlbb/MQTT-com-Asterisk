import paho.mqtt.client as mqtt
import socket

ASTERISK_HOST = "asterisk"
ASTERISK_PORT = 5038
USERNAME = "admin"
PASSWORD = "admin"

def send_ami_action(action):
    s = socket.socket()
    s.connect((ASTERISK_HOST, ASTERISK_PORT))
    s.send(f"Action: Login\r\nUsername: {USERNAME}\r\nSecret: {PASSWORD}\r\n\r\n".encode())
    s.send(action.encode())
    s.close()

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Comando recebido: {payload}")
    if payload == "ligar":
        action = (
            "Action: Originate\r\n"
            "Channel: SIP/maria\r\n"
            "Context: ligar\r\n"
            "Exten: 0800\r\n"
            "Priority: 1\r\n"
            "CallerID: MQTT\r\n\r\n"
        )
        send_ami_action(action)

client = mqtt.Client()
client.on_message = on_message
client.connect("mqtt", 1883)
client.subscribe("chamada/teste")
client.loop_forever()