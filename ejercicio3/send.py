import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='Visitas')
channel.queue_declare(queue='Resumen')
ingreso = input("ingrese palabra para buscar: ")

channel.basic_publish(exchange='',
                      routing_key='Visitas',
                      body=ingreso)
channel.basic_publish(exchange='',
                      routing_key='Resumen',
                      body=ingreso)
print(" 'consulta" + ingreso)
connection.close()
