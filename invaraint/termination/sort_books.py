# find how many days to sort list of book by swtching 2 books every days

def sorting_books(books):

    day = 0
    for i in range(len(books)):
        j = books.index(i)
        if i!=j:
            books[i],books[j] = books[j],books[i]
            print(f"after day {day} books = {books}")
            day+=1
            
books = [0, 5, 8, 1, 2, 3, 7, 4, 9, 6]

sorting_books(books)
