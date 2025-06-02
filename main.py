from sqlengine.database import Database

def main():
    db = Database()
    print("Welcome to the in-memory SQL database!")
    # TODO: Add interactive shell or script execution
    while True:
        sql = input("Enter SQL command: ")
        if sql == "exit":
            break
        print(db.execute(sql))

if __name__ == "__main__":
    main() 