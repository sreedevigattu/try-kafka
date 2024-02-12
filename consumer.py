from kafka import KafkaConsumer

# TODO: Move it to .env file or config file
# Kafka broker configuration
bootstrap_servers = 'localhost:9092'
group_id = 'test-group'

from threading import Thread

def consume(topic):
    print(f"--> consume {topic}")
    consumer = KafkaConsumer(topic,
                                group_id=group_id,
                                bootstrap_servers=bootstrap_servers,
                                auto_offset_reset='earliest')
    for message in consumer:
        value = message.value.decode('utf-8')
        print(f"[{topic}] Received message: {value}")

        d, t, msg = value.split(" ")
        if msg == 'end':
            print(f"[{topic}] ending - {d} {t}")
            break
    
    print(f"<-- consume {topic}")
        
'''import threading as t
class thread(t.Thread):
    def __init__(self, topic, thread_ID):
        t.Thread.__init__(self)
        self.topic = topic
        self.threadID = thread_ID

         # Create Kafka Consumer
        self.consumer = KafkaConsumer(topic,
                                group_id=group_id,
                                bootstrap_servers=bootstrap_servers,
                                auto_offset_reset='earliest')

    def run(self):
        print(f"--> consume {self.threadID} {self.topic}")

        for message in self.consumer:
            print(f"[{self.threadID}] Received message: {message.value.decode('utf-8')}")
        
        print(f"<--  consume {self.threadID} {self.topic}")'''

if __name__ == "__main__":
    #consume()
    '''thread1 = thread("ondu", 1)
    thread2 = thread("eradu", 2)

    thread1.start()
    thread2.start()'''

    t1 = Thread(target=consume, args = ["ondu"]); t1.start()
    t2 = Thread(target=consume, args = ["eradu"]); t2.start()

    print("main ending")