import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
content = urllib2.urlopen(url).read()
opener = "<!--\n"
closer = "\n-->"
start = content.index(opener) + len(opener)
end = content.index(closer, start)
comments = content[start:end]

regex = r"(.)\1{3,3}.(.)\2{3,3}"
regex = r"[^A-Z]+[A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][^A-Z]+"
p = re.compile(regex)
print "".join(p.findall(comments))
