import pika
from dotenv import load_dotenv
import os


load_dotenv()
ACCESS_KEY = os.environ.get('APIKey')
RABBITMQ_USER =os.environ.get('RABBITMQ_USER')
RABBITMQ_PASS =os.environ.get('RABBITMQ_PASS')

#our RabbitMQ credentials
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)

params =pika.ConnectionParameters(host='localhost',port=5672,credentials=credentials)

 
# Create a global channel variable to hold our channel object
connection = pika.BlockingConnection(params)
nairobi_channel = connection.channel()
#Create a  Queue
nairobi_channel.queue_declare(queue='lendxs')