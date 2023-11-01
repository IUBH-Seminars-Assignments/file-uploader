class MqttSubscriber():
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.qos = qos
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self._start()


    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def _start_(self):
        self.client.connect(self.host, self.port, 60)
        self.client.loop_forever()