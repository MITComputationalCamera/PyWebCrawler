# A simple script to query images using the Flickr API
# Author - Nikhil Naik (naik@mit.edu)

import flickr # flickr.py from https://code.google.com/p/flickrpy/
import os

# if you want to search for specific user - obtain  user ID from this link for 
# a specific user  : http://idgettr.com/ 
# in this case I have chosen Werner Kunz, a Boston area photographer - 
# http://www.flickr.com/photos/werkunz
id = '35375520@N07' #'XXXXXXXX@XXX' 
print "Searching for Images..."
photos = flickr.photos_search(tags='Boston',user_id = id)
print "Obtaining Image URL and Geolocation Information..." 
for photo in photos:
    url = photo.getURL(size='Medium', urlType='source') # get URL for the image
    loc = photo.getLocation() # get latitude and longitude
    cmd = 'echo %s,%s >> image_info.csv' % (url,loc)
    os.system(cmd)
