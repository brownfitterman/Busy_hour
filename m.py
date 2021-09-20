# from instaloader import *

# L = Instaloader()
# L.login("", "")
# loc = list(TopSearchResults(L.context, searchstring="Ninety Six Bar").get_locations())

# print(loc)
import json
from instaloader import *

L = Instaloader()
L.login("maidenchai2020", "Hyderabad123")
loc = list(TopSearchResults(L.context, searchstring="The Devil's Cut Restobar").get_locations())
for i in loc:

    print(i)