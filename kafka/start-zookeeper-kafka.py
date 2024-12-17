# /Applications/anaconda3/envs/alpha0.1/bin/python "/Users/yogesh-11389/MachineLearning/Private/Repository/Alpha/kafka/start-zookeeper-kafka.py"
#
import subprocess
import time
import os

# Kafka Installation Path
KAFKA_PATH = "/Users/yogesh-11389/MachineLearning/Private/Repository/Dependency/Kafka-server/kafka_2.13-3.9.0"

# Commands
ZOOKEEPER_COMMAND = [os.path.join(KAFKA_PATH, "bin/zookeeper-server-start.sh"),
                     os.path.join(KAFKA_PATH, "config/zookeeper.properties")]
KAFKA_COMMAND = [os.path.join(KAFKA_PATH, "bin/kafka-server-start.sh"),
                 os.path.join(KAFKA_PATH, "config/server.properties")]

def start_process(command_list, process_name, wait_time=5):
    """Start a shell process with error handling."""
    try:
        print(f"Starting {process_name}...")
        process = subprocess.Popen(command_list, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(wait_time)
        print(f"{process_name} started successfully.\n")
        return process
    except Exception as e:
        print(f"Error starting {process_name}:\n{e}")
        return None

def stop_process(process, process_name):
    """Stop a running process gracefully."""
    if process:
        process.terminate()
        print(f"{process_name} stopped.")

if __name__ == "__main__":
    # Start Zookeeper
    zookeeper_process = start_process(ZOOKEEPER_COMMAND, "Zookeeper")

    # Start Kafka Broker
    kafka_process = start_process(KAFKA_COMMAND, "Kafka Broker")

    # Keep the script running
    try:
        print("Kafka and Zookeeper are running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down processes...")
        stop_process(zookeeper_process, "Zookeeper")
        stop_process(kafka_process, "Kafka Broker")
