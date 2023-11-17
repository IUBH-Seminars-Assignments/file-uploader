from paho.mqtt import client as mqtt_client
from redis_client.client import rc
import uuid


class MqttClient:

    def __init__(self, host, port, topic, s_topic=None):
        self.client_id = str(uuid.uuid4())
        self.topic = topic
        self.s_topic = s_topic
        self.client = mqtt_client.Client(client_id=self.client_id)
        self.client.connect(host=host, port=port)

    def publish(self, model):
        self.client.publish(f'{self.topic}/{self.client_id}', payload=model.to_payload())

    def on_message(self, msg):
        rc.set(self.topic, msg)

    def subscribe(self):
        if self.s_topic is not None:
            self.client.subscribe(f'{self.topic}/{self.client_id}')
            self.client.on_message = self.on_message
