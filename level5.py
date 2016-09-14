import sys, urllib2, pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urllib2.urlopen(url).read())

#attempt1
for line in data:
    for elmt in line:
    	sys.stdout.write (elmt[0] * elmt[1])
    print

#attempt2    
for line in data:
    print ''.join(elmt[0] * elmt[1] for elmt in line)


