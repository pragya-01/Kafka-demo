# Kafka-demo
Hands-on kafka


# command to check the topics created
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

# command to know about the topic
docker exec -it kafka kafka-topics  --bootstrap-server localhost:9092 --describe --topic orders


# check all the events
 docker exec -it kafka kafka-console-consumer  --bootstrap-server localhost:9092  --topic orders --from-beginning



 ^CTraceback (most recent call last):
  File "/Users/pragya.b.agrawal/Desktop/Personal_Projects/Kafka-demo/tracker.py", line 25, in <module>
    msg=consumer.poll(1.0)
KeyboardInterrupt -> python error