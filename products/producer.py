import pika, json
import time

def get_connection():
	while True:
		try:
			return pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, heartbeat=600,  # Send a heartbeat every 10 minutes
        	blocked_connection_timeout=300))
		except pika.exceptions.AMQPConnectionError:
			print("Connection lost, retrying in 5 seconds...")
			time.sleep(5)


def publish(method, body):
	connection = get_connection()
	channel = connection.channel()
	channel.queue_declare(queue='main')
	try:
		properties = pika.BasicProperties(method)
		channel.basic_publish(exchange='',
						routing_key='main',
						body=json.dumps(body),
						properties=properties)
	except pika.exceptions.StreamLostError:
		print("Connection lost while publishing, retrying...")
		publish(method, body)\

	print(" [x] Sent body")
	connection.close()
