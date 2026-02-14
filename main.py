from stats import wordCount, characterCount
#from stats import characterCount


#reads in a book when provided with a file path
def get_book_text(filePath):
    
    with open(filePath) as book:
        return book.read()
        
        
#counts the words contained in a string that it is passed split on ' '
#def wordCount(wordsToCount):
#    
#    splitBook = wordsToCount.split()
#    print(len(splitBook))
#    return len(splitBook)
    
    
#run it all
def main():
    
    #print the book out
    #print(get_book_text("./books/frankenstein.txt"))
    
    #print the wordcount of a book
    print("Found " + str(wordCount(get_book_text("./books/frankenstein.txt"))) + " total words")
    print(characterCount(get_book_text("./books/frankenstein.txt")))

    
    
    
    
    
main()
    
    
    
    
