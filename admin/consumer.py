import pika

params = pika.URLParameters('amqps://wwwikjkc:pUD8_GzUi7O_w4cldiQyZVstok7LBxf4@toad.rmq.cloudamqp.com/wwwikjkc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print ('Reveived in admin')
    print (body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print ('Started Cosuming')

channel.start_consuming()

channel.close()