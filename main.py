from stats import wordCount, characterCount, sortedDictionary
#from stats import characterCount


#reads in a book when provided with a file path
def get_book_text(filePath):
    
    with open(filePath) as book:
        return book.read()
        
    
    
#run it all
def main():
    
    bookLocation = "books/frankenstein.txt"
    
    #print the book out
    #print(get_book_text("./books/frankenstein.txt"))
    
    #print the wordcount of a book
    #print("Found " + str(wordCount(get_book_text("./books/frankenstein.txt"))) + " total words")
    
    #print the character count of a book
    #print(characterCount(get_book_text("./books/frankenstein.txt")))
    
    #print the sorted character count of the book with alpha characters only
    #print(sortedDictionary(characterCount(get_book_text("./books/frankenstein.txt"))))
    
    #run the function to make formatting the output later a little nicer
    sortedData = sortedDictionary(characterCount(get_book_text("./" + bookLocation)))
    
    
    #print the final output
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(bookLocation) + "...")
    print("----------- Word Count ----------")
    print("Found " + str(wordCount(get_book_text("./" + bookLocation))) + " total words")
    print("--------- Character Count -------")
    
    for char, count in sortedData.items():
        print(char + ": " + str(count))
        
    print("============= END ===============")

    
    
main()
    
    
    
    
