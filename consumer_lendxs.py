from config import  nairobi_channel, connection
import  sys, os

def on_message(channel, method_frame, header_frame, body):
    '''Called When we  receive a message from RabbitMq'''
    print(method_frame.delivery_tag)
    print(body)
    print(header_frame)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
def consumeFromRabbitMq(channel, q_name, connection):
   
    
    channel = connection.channel()
   
    channel.queue_declare(queue=q_name)
    
    channel.basic_consume(queue=q_name,on_message_callback=on_message, auto_ack=True)
    
    print('Waiting for messages.')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        consumeFromRabbitMq(channel=nairobi_channel, q_name='lendxs', connection=connection)
    except KeyboardInterrupt:
        print('Interrupted by Keyboard..')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)  
    