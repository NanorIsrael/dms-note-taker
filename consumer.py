import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rmq',port=5672))
channel = connection.channel()
channel.queue_declare("dms")

def callback(ch, method, properties, body):
	print(body)

channel.basic_consume(queue='dms', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
channel.basic_consume()