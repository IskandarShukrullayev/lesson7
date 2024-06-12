import multiprocessing
import time
from datetime import datetime
def write_to_file(file_path: str , data: str ):
    time.sleep(3)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f"Data written to {file_path}\n")

def main():
    file_path1 = 'data/data1.txt'
    file_path2 = 'data/data2.txt'
    file_path3 = 'data/data3.txt'
    file_path4 = 'data/data4.txt'
    data1 = 'Hello from Process 1!'
    data2 = 'Greetings from Process 2!'
    data3 = 'Hi python 3!'
    data4 = ' Hello world 4!'

    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4))

    # Start processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())