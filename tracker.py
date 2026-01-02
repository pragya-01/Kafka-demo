from confluent_kafka import Consumer
import json

consumer_config= {
    'bootstrap.servers':'localhost:9092',
    #a unique string that identifies the consumer group this consumer belongs to
    "group.id":"order-tracker",
    #what to do if it cannot find where it got left off
    "auto.offset.reset":"earliest"

}

consumer= Consumer(consumer_config)

consumer.subscribe(["orders"])


print("Consumer is running and subscruibed to orders topic")


#gracefully shut down the consumer app
try:
    #to check actively if there is a new event
    #polling is basically consumer messaging kafka to know about new events
    #that way consumer has more ownership in terms of events it wants to handle
    while True:
        msg=consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error:", msg.error())
            continue

        value=msg.value().decode("utf-8")
        order = json.loads(value)

        print(f"Recieved Order: {order['quantity']} * {order['item']} from {order['user']}")

except KeyboardInterrupt:
    print("\n Stopping Consumer")

finally:
    consumer.close()
   

