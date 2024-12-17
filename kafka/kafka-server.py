# /Applications/anaconda3/envs/alpha0.1/bin/python "/Users/yogesh-11389/MachineLearning/Private/Repository/Alpha/kafka/kafka-server.py"     
#

from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simulated real-time data
while True:
    data = {"symbol": "RELIANCE", "price": round(random.uniform(2500, 2700), 2)}
    producer.send('stock_prices', value=data)
    print(f"Sent: {data}")
    time.sleep(1)

