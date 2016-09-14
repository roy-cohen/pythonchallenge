import re, zipfile

baseDir = '/thepythonchallenge/' #change to correct directory
channelDir = baseDir + 'channel/'
extension = '.txt'
fileName = '90052' + extension
filePath = channelDir + fileName
digits = '\d+'

channelZip = zipfile.ZipFile(baseDir + "channel.zip")
comments = channelZip.getinfo(fileName).comment
data = open(filePath).read()
found = re.search(digits, data)
try:
    while found.group(0):
        fileName = found.group(0) + extension
        filePath = channelDir + fileName
        comments += channelZip.getinfo(fileName).comment
        data = open(filePath).read()
        found = re.search(digits, data)	
except AttributeError:
    pass

print comments

# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

#oxygen