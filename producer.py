from kafka import KafkaProducer
import time, random
from datetime import datetime 

# Kafka broker configuration
bootstrap_servers = 'localhost:9092'
topic = 'ondu' #'quickstart-events'

# Create Kafka Producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def produce():
    print("--> produce")

    for i in range(10):
        # Produce message asynchronously
        topic = "ondu" if random.randint(1, 2) == 1 else "eradu"
        message = f'Message{datetime.now()} {topic} {i}'
        producer.send(topic, message.encode('utf-8'))
        print(f"Sending message: {message}")
        time.sleep(1)

    print("Sending end messages...")
    message = f'Message{datetime.now()} end'
    producer.send("ondu",  message.encode('utf-8'))
    producer.send("eradu", message.encode('utf-8'))

    print("<-- produce")

if __name__ == '__main__':
    produce()