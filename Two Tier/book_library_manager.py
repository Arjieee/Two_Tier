import mysql.connector # type: ignore

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Change if you have another MySQL user
        password="As@111521",  # Set your MySQL password
        database="library_db"
    )

def create_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            year INT
        )
    """)
    db.commit()
    db.close()

def add_book(title, author, year):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
    db.commit()
    db.close()
    print("✅ Book added successfully!")

def view_books():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    for book in cursor.fetchall():
        print(book)
    db.close()

def update_book(book_id, title, author, year):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s", (title, author, year, book_id))
    db.commit()
    db.close()
    print("✅ Book updated successfully!")

def delete_book(book_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    db.commit()
    db.close()
    print("✅ Book deleted successfully!")

if __name__ == "__main__":
    create_table()
    while True:
        print("\n📚 Book Library Manager")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            add_book(title, author, year)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = input("Enter book ID to update: ")
            title = input("New title: ")
            author = input("New author: ")
            year = input("New year: ")
            update_book(book_id, title, author, year)
        elif choice == "4":
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice, try again.")
