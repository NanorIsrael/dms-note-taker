import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='dms')
def publish():
	channel.basic_publish(exchange='',
                      routing_key='dms',
                      body='Hello World!')
	print(" [x] Sent 'Hello World!'")
	connection.close()


