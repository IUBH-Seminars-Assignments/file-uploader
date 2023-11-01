from paho.mqtt import client as mqtt_client
from flask import jsonify
#import redis.client as redisc
from redis_client.client import rc
import uuid

class MqttClient:

    def __init__(self, host, port, topic):
        self.client_id=str(uuid.uuid4())
        self.topic = topic
        self.client = mqtt_client.Client(client_id=self.client_id)
        self.client.connect(host=host, port=port)

    def publish(self, model):
        self.client.publish(f'{self.topic}/{self.client_id}', payload=model.to_payload())

    def on_message(self, msg):
        rc.set(self.topic, msg)

    def subscribe(self):
        self.client.subscribe(f'{self.topic}/{self.client_id}')
        self.client.on_message = self.on_message

    