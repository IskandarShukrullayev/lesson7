import threading
import time
from datetime import datetime

def read_file(file_path):
    time.sleep(3)
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}")

def main():
    file_path1 = 'data/data1.txt'
    file_path2 = 'data/data2.txt'
    file_path3 = 'data/data3.txt'
    file_path4 = 'data/data4.txt'

    # Create threads
    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))
    thread3 = threading.Thread(target=read_file, args=(file_path3,))
    thread4 = threading.Thread(target=read_file, args=(file_path4,))



    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("Main thread continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())
