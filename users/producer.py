# # users/producer.py

# from confluent_kafka import Producer
# import json

# p = Producer({'bootstrap.servers': 'localhost:9092'})

# def delivery_report(err, msg):
#     if err is not None:
#         print('Message delivery failed: {}'.format(err))
#     else:
#         print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# def produce_user_data(user_data):
#     p.produce('user_validations', key=user_data['email'], value=json.dumps(user_data), callback=delivery_report)
#     p.flush()
