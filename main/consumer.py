import pika

params = pika.URLParameters('amqps://wwwikjkc:pUD8_GzUi7O_w4cldiQyZVstok7LBxf4@toad.rmq.cloudamqp.com/wwwikjkc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print ('Reveived in main')
    print (body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print ('Started Cosuming')

channel.start_consuming()

channel.close()