import pika

params = pika.URLParameters('amqps://wwwikjkc:pUD8_GzUi7O_w4cldiQyZVstok7LBxf4@toad.rmq.cloudamqp.com/wwwikjkc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body='hello main', body=json.dumps(body), properties=properties)