import sys
import json
import numpy as np
from base64 import encodebytes, decodebytes
import base64


##------------------------------##
# input : se_list (string)
# output : dic (xtype(string). xdata(np.array or string), ytype(string), ydata(np.array or string))
##------------------------------##

def on_run(stringdata):
	strdata = "".join([chr(item) for item in stringdata])
	sdata = json.loads(decodebytes(strdata.encode('utf-8')).decode('utf-8'))
	sdata = np.array(sdata, dtype=np.float32)
	return {"data": sdata}
