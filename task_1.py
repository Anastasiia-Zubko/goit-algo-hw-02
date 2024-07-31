"""
Task 1: processing requests
"""

from queue import Queue
import random
from time import sleep

# Initialize the queue
queue = Queue()

def generate_request():
    """
    Generate a new request and add it to the queue.
    """
    new_request = random.randint(1, 1000)
    queue.put(new_request)
    print(f"Added: {new_request}")

def process_request():
    """
    Process a request by removing it from the queue.
    """
    if not queue.empty():
        request = queue.get()
        print(f"Processed: {request}")
    else:
        print("The queue is empty")

def main():
    """
    Main function to execute generate_request process_request functions.
    """
    try:
        while True:
            generate_request()
            process_request()
            sleep(0.2)
    except KeyboardInterrupt:
        print("Finish the processing")

if __name__ == "__main__":
    main()
