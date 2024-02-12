# try-kafka
Kafka is a distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

ZooKeeper Manages and coordinates distributed systems in general. 
Specifically for kafka , it manages and coordinates  brokers that make up a kafka cluster.
Keeps track of 
which brokers are part of the kakfa cluster
which broker is the leader of a given partition and topic
Tracks the status of nodes in kafka
Maintain a list of Kafka topics and messages

broker partition topic record durable
one-to-one
one-to-many
many-to-many

filter aggregate enrich


## Run
1. Start ZooKeeper
    cd C:\MyInstalls\kafka
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
2. Run kafka server
    cd C:\MyInstalls\kafka
    .\bin\windows\kafka-server-start.bat .\config\server.properties

- Create Topic
cd C:\MyInstalls\kafka\bin\windows
kafka-topics.bat --bootstrap-server localhost:9092 --describe  
kafka-topics.bat --bootstrap-server localhost:9092 --create --topic TEST
kafka-topics.bat --bootstrap-server localhost:9092 --delete --topic TEST 

- Run Producer
kafka-console-producer. --topic TEST --bootstrap-server localhost:9092

- Run consumer - gets messages from this instant
kafka-console-consumer.bat --topic ondu --bootstrap-server localhost:9092
kafka-console-consumer.bat --topic ondu --from-beginning --bootstrap-server localhost:9092

- Delete messages 
delete C:\MyInstalls\kafka\kafka-logs
delete C:\MyInstalls\kafka\zookeeper-data

## Installation 
Windows

## Apache Server
1. Download
2. Install 
3. Configure
4. Start ZooKeeper
    cd C:\MyInstalls\kafka
    .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
5. Run kafka server
    cd C:\MyInstalls\kafka
    .\bin\windows\kafka-server-start.bat .\config\server.properties


## Python code
pip install kafka-python