import urllib.request
import os
from bs4 import BeautifulSoup

def recursiveFlag(addr):
    f = urllib.request.urlopen(addr)
    soup = BeautifulSoup(f.read())
    for path in soup.find_all('a'):
        href = path.get('href')
        if (href.endswith('/') and not href.startswith('.')):
            recursiveFlag(addr + href)
        elif (not href.startswith('.')):
            os.system('curl ' + addr + href + ' >> ./scrappedDatas')

# depends on address of target machine
recursiveFlag('http://192.168.56.102/.hidden/')
