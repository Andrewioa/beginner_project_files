genre = {'Fiction':[],
         'Non Fiction':[],
         'Horror':[]
         }
def book_read(x):
    #ask = input('Enter a book you read: ')
    g = input('What genre is it? ').capitalize()
    if g in genre:
        genre[g] = x
    else:
        genre[g] = x
    print(genre)


print(genre)







