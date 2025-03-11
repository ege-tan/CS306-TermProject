from pymongo import MongoClient
from pymongo import errors

def connectDB():
    # Replace the connection string with your MongoDB connection string
    # You can obtain the connection string from your MongoDB Atlas dashboard or configure it locally
    # For example, if your database is running on localhost, the connection string might look like this:
    # "mongodb://localhost:27017/"

    connection_string = "mongodb+srv://admin:admin@phase4.4gndiul.mongodb.net/?retryWrites=true&w=majority&appName=phase4"
    client = MongoClient(connection_string)

    # Access a specific database (replace "your_database_name" with your actual database name)
    db = client.phase4
    print("Connection established to your db")
    return db

def create_collection(db, collection_name):
    try:
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        elif collection_name in db.list_collection_names():
            print("Collection already exists")
    except Exception as e:
        print("An error occurred: ", e)

def insert_data(db, collection_name, data):
    try:
        collection = db[collection_name]
        existing_entry = collection.find_one({"id": data["id"]})
        if existing_entry:
            print(f"An entry with ID '{data['id']}' already exists.")
        else:
            collection.insert_one(data)
            print("Data inserted successfully!")
    except errors.PyMongoError as e:
        print(f"An error occurred while inserting data: {e}")

def read_all_data(db, collection_name):
    try:
        collection = db[collection_name]
        for document in collection.find():
            print(document)
    except errors.PyMongoError as e:
        print(f"An error occurred while reading data: {e}")

def read_filtered_data(db, collection_name, value):
    try:
        collection = db[collection_name]
        filter_criteria = {"given_star": {"$gt": value}}
        documents = collection.find(filter_criteria)
        results = list(documents)
        if results:
            for document in results:
                print(document)
        else:
            print("No documents found with the given filter.")
        return results
    except errors.PyMongoError as e:
        print(f"An error occurred while reading data: {e}")
        return []

def update_data(db, collection_name, entry_id, update):
    try:
        collection = db[collection_name]
        existing_entry = collection.find_one({"id": entry_id})
        if not existing_entry:
            print(f"No entry found with ID '{entry_id}'.")
        else:
            collection.update_one({"id": entry_id}, {"$set": update})
            print("Data updated successfully!")
    except errors.PyMongoError as e:
        print(f"An error occurred while updating data: {e}")

def delete_data(db, collection_name, entry_id):
    try:
        collection = db[collection_name]
        existing_entry = collection.find_one({"id": entry_id})
        if not existing_entry:
            print(f"No entry found with ID '{entry_id}'.")
        else:
            collection.delete_one({"id": entry_id})
            print("Data deleted successfully!")
    except errors.PyMongoError as e:
        print(f"An error occurred while deleting data: {e}")

def list_collections(db):
    collections = db.list_collection_names()
    for i, collection in enumerate(collections, start=1):
        print(f"{i} - {collection}")
    return collections

def main():
    db = connectDB()

    while True:
        print("\nPlease select an operation:")
        print("1 - Create collection")
        print("2 - Read all data in a collection")
        print("3 - Read some part of the data while filtering")
        print("4 - Insert data")
        print("5 - Delete data")
        print("6 - Update data")
        print("7 - Exit")

        choice = input("Your choice: ")

        if choice == "1":
            collection_name = input("Name of the collection to create: ")
            create_collection(db, collection_name)
        elif choice == "2":
            print("Please select the collection you want to read data from:")
            collections = list_collections(db)
            collection_choice = int(input("Selected option: ")) - 1
            if 0 <= collection_choice < len(collections):
                collection_name = collections[collection_choice]
                read_all_data(db, collection_name)
            else:
                print("Invalid selection.")
        elif choice == "3":
            print("Please select the collection you want to read data from:")
            collections = list_collections(db)
            collection_choice = int(input("Selected option: ")) - 1
            if 0 <= collection_choice < len(collections):
                collection_name = collections[collection_choice]
                value = int(input("Filter acc to 'given_star' (greater than): "))
                read_filtered_data(db, collection_name, value)
            else:
                print("Invalid selection.")
        elif choice == "4":
            print("Please select the collection you want to insert data into:")
            collections = list_collections(db)
            collection_choice = int(input("Selected option: ")) - 1
            if 0 <= collection_choice < len(collections):
                collection_name = collections[collection_choice]
                entry_id = input("Enter ID for the entry: ")  # Ask user for ID
                name = input("Name: ")
                review_message = input("Review message: ")
                given_star = int(input("Given star (out of 5): "))
                data = {
                    "id": entry_id,
                    "name": name,
                    "review_message": review_message,
                    "given_star": given_star
                }
                insert_data(db, collection_name, data)
            else:
                print("Invalid selection.")
        elif choice == "5":
            print("Please select the collection you want to delete data from:")
            collections = list_collections(db)
            collection_choice = int(input("Selected option: ")) - 1
            if 0 <= collection_choice < len(collections):
                collection_name = collections[collection_choice]
                entry_id = input("Enter ID of the record to delete: ")
                delete_data(db, collection_name, entry_id)
            else:
                print("Invalid selection.")
        elif choice == "6":
            print("Please select the collection you want to update data in:")
            collections = list_collections(db)
            collection_choice = int(input("Selected option: ")) - 1
            if 0 <= collection_choice < len(collections):
                collection_name = collections[collection_choice]
                entry_id = input("Enter ID of the record to update: ")
                update_field = input("Field to update: ")
                update_value = input("New value: ")
                update_data(db, collection_name, entry_id, {update_field: update_value})
            else:
                print("Invalid selection.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()