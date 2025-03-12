import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='main')
def publish():
	channel.basic_publish(exchange='',
                      routing_key='main',
                      body='Hello World!')
	print(" [x] Sent 'Hello World!'")
	# connection.close()


