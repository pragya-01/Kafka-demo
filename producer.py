from confluent_kafka import Producer
import uuid
import json


producer_config={
    'bootstrap.servers':'localhost:9092'
}

#provides the intial hosts that act as the starting point for a kafka client
producer= Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"Delivery Failed: {err}")
    else:
        msg1=msg.value().decode("utf-8")
        print(f"Delivered {msg1}")
        print(f"Delivered to {msg.topic()} : partition {msg.partition()} at offset {msg.offset()}")

order = {
    "order_id": str(uuid.uuid4()),
    "user":"nicole",
    "item":"rice bowl",
    "quantity":1
}

#convert json into bytes which kafka can understand
value = json.dumps(order).encode("utf-8")

#please save this in topic called orders, if topic doesn't exist, it will automatically create the topic
producer.produce( 
    topic="orders", 
    value=value,
    callback=delivery_report
)

#kafka b uffers the events, it doesn't send event one by one. It sends in batches
#this command helps in case of failures to send the event which are in buffer before crasing out or exiting out 
producer.flush()










