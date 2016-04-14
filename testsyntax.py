__author__ = 'Tejal'

import numpy as np

# twodarray = [[1,2],[3,4],[5,6]]
# if 3 in twodarray[0:2]:
#     print "true"
# else:
#     print "false"

# dict = {"key":{}}
# dict["key"][0]=1
# dict["key"][2]=3
# dict["key"][3]=dict["key"][2]+2
# print(dict["key"][3])

ndarray = np.array([[1,2,3],[7,8,9]])
ndarray = np.concatenate((ndarray,[4,5,6]),axis=0)
print(ndarray)