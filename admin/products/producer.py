import pika

params = pika.URLParameters('amqps://wwwikjkc:pUD8_GzUi7O_w4cldiQyZVstok7LBxf4@toad.rmq.cloudamqp.com/wwwikjkc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')