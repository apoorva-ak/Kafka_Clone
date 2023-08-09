# Kafka_Clone

Implemented as a part of Big Data course at PES University to gain a better understanding of Kafka Architecture

# Features:
- To set up a mini-Kafka on local system, consisting of Producers, Subscribers, Brokers and Zookeeper.
- Uses socket programming, subprocess module libraries
- Dynamic number of producers, consumers and topics could be created by user.
- Topics created as directories within file structure
- Partitioning and replication also implemented

# Steps:
1. Clone the repository
2. Navigate to project directory
3. Open terminal within project directory and run: python3 zookeeper.py
4. Open another terminal to start the producers and choose the number of producers: python3 producer_controller.py
5. Start the consumers and choose the number of consumers: python3 consumer_controller.py
