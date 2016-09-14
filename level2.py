import collections

#attempt 

file = open('ocr.html', 'r')
content = file.read()
opener = "<!--\n"
closer = "\n-->"
start = content.index(opener)
start = content.index(opener, start + 1) + len(opener)
end = content.index(closer, start)
comments = content[start:end]

d = collections.OrderedDict()

for ch in comments:
    key = ch		
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

s = ""
for key in d.keys():
	if d[key] == 1:
	    s += key

print s 


#attempt2

d = {}
for ch in comments:
    d[ch] = d.get(ch, 0) + 1

print "".join(ch for ch in comments if d[ch] == 1)
