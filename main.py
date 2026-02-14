import sys
from stats import wordCount, characterCount, sortedDictionary



#reads in a book when provided with a file path
def get_book_text(filePath):
    
    with open(filePath) as book:
        return book.read()
        
    
    
#run it all
def main():
    
    bookLocationHardCoded = "books/frankenstein.txt"
    bookLocationDynamic = ""
    
    if len(sys.argv) != 2:
        
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        bookLocationDynamic = sys.argv[1]
    
        #print the book out
        #print(get_book_text("./books/frankenstein.txt"))
        
        #print the wordcount of a book
        #print("Found " + str(wordCount(get_book_text("./books/frankenstein.txt"))) + " total words")
        
        #print the character count of a book
        #print(characterCount(get_book_text("./books/frankenstein.txt")))
        
        #print the sorted character count of the book with alpha characters only
        #print(sortedDictionary(characterCount(get_book_text("./books/frankenstein.txt"))))
        
        #run the function to make formatting the output later a little nicer
        sortedData = sortedDictionary(characterCount(get_book_text(bookLocationDynamic)))
        
        
        #print the final output
        print("============ BOOKBOT ============")
        print("Analyzing book found at " + str(bookLocationDynamic) + "...")
        print("----------- Word Count ----------")
        print("Found " + str(wordCount(get_book_text(bookLocationDynamic))) + " total words")
        print("--------- Character Count -------")
        
        for char, count in sortedData.items():
            print(char + ": " + str(count))
            
        print("============= END ===============")

    
    
main()
    
    
    
    
