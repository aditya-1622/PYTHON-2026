# LIBRARY MANAGEMENT SYSTEM

library = []

# function to add book
def add_book(book_id, title, author, copies):
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "copies": copies,
        "borrowed_by": []
    }
    library.append(new_book)
    print(f"Added book: '{title}' by {author} ({copies} copies)")


# function to show books
def show_books():
    print("ALL BOOKS")

    if len(library) == 0:
        print("No books yet.")
        return

    for book in library:
        print(f"ID {book['id']}: '{book['title']}' by {book['author']} "
              f"-> {book['copies']} copies left")


# function to find book by ID
def find_book_by_id(book_id):
    for book in library:
        if book["id"] == book_id:
            return book
    return None   # loop ke BAAHAR - saari books check karne ke baad


# function to borrow book
def borrow_book(book_id, person_name):
    book = find_book_by_id(book_id)

    if book is None:
        print("That book doesn't exist")
        return

    if book["copies"] <= 0:
        print(f"Sorry, '{book['title']}' has no copies available right now.")
        return

    book["copies"] -= 1
    book["borrowed_by"].append(person_name)
    print(f"{person_name} borrowed '{book['title']}'. "
          f"{book['copies']} copies left.")


# function to return book
def return_book(book_id, person_name):
    book = find_book_by_id(book_id)

    if book is None:
        print("That book doesn't exist")
        return

    if person_name not in book["borrowed_by"]:
        print(f"{person_name} did not borrow '{book['title']}'.")
        return

    book["borrowed_by"].remove(person_name)
    book["copies"] += 1
    print(f"{person_name} returned '{book['title']}'. "
          f"{book['copies']} copies now available.")


# function to search book by title
def search_by_title(keyword):
    print(f"\nSearch Result for '{keyword}'")
    found_any = False

    for book in library:
        if keyword.lower() in book["title"].lower():
            print(f"ID {book['id']}: '{book['title']}' by {book['author']}")
            found_any = True

    if not found_any:
        print("No books matched your search.")


# MAIN PROGRAM - ye top-level pe hona chahiye, kisi function ke andar nahi
if __name__ == "__main__":
    add_book(1, "Something I Never Told You", "Shravya Bhinder", 2)
    add_book(2, "Me Before You", "Jojo Moyes", 1)
    add_book(3, "I Don't Love You Anymore", "Rithvik Singh", 3)

    show_books()

    borrow_book(1, "Aditya")
    borrow_book(2, "Adi")
    borrow_book(2, "Palak")   # error dega, copy available nahi hai

    show_books()

    return_book(1, "Aditya")

    search_by_title("Something")

    show_books()