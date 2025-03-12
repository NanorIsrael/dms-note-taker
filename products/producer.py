import pika, json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='main')

def publish(method, body):
	properties = pika.BasicProperties(method)
	channel.basic_publish(exchange='',
                      routing_key='main',
                      body=json.dumps(body),
					  properties=properties)
	print(" [x] Sent body")
	# connection.close()


