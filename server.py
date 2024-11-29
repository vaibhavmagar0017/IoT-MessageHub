import pika
import pymongo
import json


def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received: {message}")
    collection.insert_one(message)


def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='mqtt', exchange_type='direct')
    queue = channel.queue_declare(queue='', exclusive=True).method.queue
    channel.queue_bind(exchange='mqtt', queue=queue, routing_key='status')

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mqtt_db"]
    collection = db["messages"]
    consume_messages()
