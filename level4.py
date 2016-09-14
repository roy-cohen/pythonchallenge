import urllib2

def keepGoing(urlBase, nextNum) :
	
    searchTerm = "next nothing is "
    try:
		while True:
		    contents = urllib2.urlopen(urlBase + nextNum).read()
		    print contents
		    index = contents.index(searchTerm, 0, len(contents)) + len(searchTerm)
		    nextNum = contents[index:]
    except ValueError:
	    pass

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nextNum = "12345"

keepGoing(urlbase, nextNum)
# and the next nothing is 16044
# Yes. Divide by two and keep going.
print 16044 / 2

nextNum = "8022"
keepGoing(urlbase, nextNum)
#peak.html