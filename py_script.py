# Download, process, and Plot Sounding Data from University of Wyoming

import urllib2
from bs4 import BeautifulSoup
from skewt import SkewT

stn = '72572' #72572 is ID for SLC
year= '2015'
month = '06'
day = '12'
hour = '12' #either 12 or 00

# 1)
# Wyoming URL to download Sounding from
url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR='+year+'&MONTH='+month+'&FROM='+day+hour+'&TO='+day+hour+'&STNM='+stn
content = urllib2.urlopen(url).read()

# 2)
# Remove the html tags
soup = BeautifulSoup(content)
data_text = soup.get_text()

# 3)
# Split the content by new line.
splitted = data_text.split("\n",data_text.count("\n"))

# 4)
# Write this splitted text to a .txt document
Sounding_filename = str(stn)+'.'+str(year)+str(month)+str(day)+str(hour)+'.txt'
f = open(Sounding_filename,'w')
for line in splitted[4:]:
    f.write(line+'\n')
f.close()

# 5)
sounding = SkewT.Sounding(filename=Sounding_filename)
sounding.plot_skewt()
