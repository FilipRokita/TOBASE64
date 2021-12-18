#TOBASE64
#Filip Rokita
#www.filiprokita.com

import base64
import sys



filedir = sys.argv[1]

f = open(filedir, 'rb')
data = f.read()
f.close()

b64 = base64.b64encode(data)
b64 = str(b64)
b64 = b64[2:-1]

f = open(filedir+'.b64', 'w')
f.write(b64)
f.close()