books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict=dict()
for book in books:
  key=book
  lenght=len(book)
  x=len(set(key))
  a=(x+lenght)/2
  a=int(a)
  value=(lenght,x,a)
  book_dict[key]=value
print(book_dict)
