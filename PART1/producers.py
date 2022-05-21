import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

# sets to default if we dont pass parameters
channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "Hello this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"message send: {message}")

connection.close()