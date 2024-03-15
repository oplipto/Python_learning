import requests

def random_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        books_data = data["data"]
        book = books_data["volumeInfo"]["title"]
        book_published = books_data["volumeInfo"]["publishedDate"]
        return book, book_published
    else:
        raise Exception("Failed to fetch jokes")
    

def main():
    try:
        book = random_books()
        print(f"Book: {book[0]}\nPublished: {book[1]}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()