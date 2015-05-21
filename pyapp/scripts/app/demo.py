import sys
import string
import random

sys.path.insert(0, 'src')
import urlbase

global possible_chars

# URL generator
# Generates count number of URL strings of size size
# and containing chars
def URLsGenerator(count=10, size=10, chars=string):
    urlCollection = [""]*count
    for i in range(count):
        urlCollection[i] = 'www.' + ''.join(random.choice(chars) for _ in range(size)) + '.com'
    return urlCollection

if __name__ == "__main__":    
    possible_chars = 'abcdefghijklmnopqrstuvwxyz'
    error = urlbase.Init('192.168.1.10','6379')
    if error == False:
        print 'Welcome to demonstration for python-lib'
        
        print '\nGenerating 10 random URLs for the demo...'
        urls = URLsGenerator(10, 10, possible_chars)
        for i in range(len(urls)):
                print urls[i] 

        print '\nStoring URLs into urlbase (Redis DB client)...'
        counter = 0
        for i in range(len(urls)):
            error = urlbase.Store(i, urls[i])
            if error:
                print 'Failed to store', urls[i]
            else:
                counter = counter + 1
                print 'Stored', urls[i]                
        print 'Stored', counter, 'URLs!'

        print '\nRetrieving URLs from urlbase...'
        counter = 0
        retrievedURLs = ['']*10
        for i in range(len(retrievedURLs)):
            someurl = urlbase.Fetch(i)
            if someurl is None:
                print 'Failed to retrive URL at ID', i
            else:
                counter = counter + 1
                retrievedURLs[i] = someurl
                print 'Retrieved', someurl, 'Matched', retrievedURLs[i] == urls[i]        
        print 'Retrieved', counter, 'URLs!'
