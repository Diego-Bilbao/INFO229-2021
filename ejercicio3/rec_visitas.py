import pika, sys, os, pageviewapi.period

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='Visitas')
    def callback(ch, method, properties, body):
        aux = pageviewapi.period.sum_last("en.wikipedia", body.decode(), last=365, access='all-access', agent='all-agents')
        print(" Visitas: %r" % aux)
    channel.basic_consume(queue='visitas', on_message_callback=callback, auto_ack=True)
    print(' Esperando, para salir presione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

