#importing the required modules
from json import loads
from kafka import KafkaConsumer

# generating the Kafka Consumer
my_consumer = KafkaConsumer(
'quickstart-events',
bootstrap_servers = ['localhost : 9092'],
group_id = 'my-group')
print(my_consumer)
for message in my_consumer:
     print(message.value)
