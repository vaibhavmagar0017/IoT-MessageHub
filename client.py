import pika
import json
import time
import random

def publish_messages():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            port=5672,
            credentials=pika.PlainCredentials('testuser', 'testpassword')
        )  # Adjust host/port if necessary
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='mqtt', exchange_type='direct')

    try:
        while True:
            message = {"status": random.randint(0, 6), "timestamp": time.time()}
            channel.basic_publish(exchange='mqtt', routing_key='status', body=json.dumps(message))
            print(f"Sent: {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped publishing messages.")
    finally:
        connection.close()

if __name__ == "__main__":
    publish_messages()
