import threading
import time

# Event to signal the termination of thread1
stop_event = threading.Event()

def function1():
    for _ in range(5):
        time.sleep(1)
        print("Function 1 working...")
    print("Function 1 completed.")
    stop_event.set()  # Set the event to signal completion

def function2():
    while not stop_event.is_set():
        time.sleep(1)
        print("Function 2 working...")
    print("Function 2 stopped because Function 1 completed.")

# Create threads for each function
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)

# Start the threads
thread1.start()
thread2.start()

# Wait for thread1 to finish
thread1.join()

# Wait for thread2 to finish
thread2.join()

print("Both functions have completed.")



# import threading
# import time

# def function1():
#     for _ in range(5):
#         time.sleep(1)
#         print("Function 1 working...")

# def function2():
#     for _ in range(5):
#         time.sleep(1)
#         print("Function 2 working...")

# # Create threads for each function
# thread1 = threading.Thread(target=function1)
# thread2 = threading.Thread(target=function2)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

# print("Both functions have completed.")
