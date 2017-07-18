import urllib2
f=urllib2.urlopen(http://meidensha.co,jp/)
htmlSource = f.read()
print htmlSource
