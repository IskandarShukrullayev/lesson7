from database import database
import multiprocessing

query1 = {
    'query1': "INSERT INTO users VALUES('adis', 23)",
    'query2': "INSERT INTO users VALUES('bob', 20)",
    'query3': "INSERT INTO users VALUES('john', 18)",
    'query4': "INSERT INTO users VALUES('ada', 24)",
    'query5': "INSERT INTO users VALUES('rasul', 28)",
    'query6': "INSERT INTO users VALUES('asad', 16)",
}

query2 = {
    'query1': "INSERT INTO courses VALUES('python', 23)",
    'query2': "INSERT INTO courses VALUES('c#', 20)",
    'query3': "INSERT INTO courses VALUES('c++', 18)",
    'query4': "INSERT INTO courses VALUES('java', 24)",
    'query5': "INSERT INTO courses VALUES('smm', 28)",
    'query6': "INSERT INTO courses VALUES('c', 16)",
}

def insert_data(query, query_type):
    print(Database.connect(query, query_type))

    def process():
        query1: "INSERT INTO courses VALUES('python', 23)"
        query2: "INSERT INTO courses VALUES('c#', 20)"
        query_type1 = "insert"
        query_type2 = "insert"

        process1 = multiprocessing.process(target=insert_data, args=[query1, query_type1])
        process2 = multiprocessing.process(target=insert_data, args=[query2, query_type2])

        process1.start()
        process2.start()

        process1.join()
        process2.join()

if __name__ == "__main__":
    print(datetime.now())
    process()
    print(datetime.now())
