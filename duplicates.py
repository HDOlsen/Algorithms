#a set is GUARANTEED not to yield duplicates
def duplicate():
    names = ["Alex" , "John" , "Mary" , "Steve" , "John" , "Steve"]
    names = (set(names))
    print(names)

duplicate()

