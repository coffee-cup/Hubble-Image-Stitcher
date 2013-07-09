#!hubbleimagestitcher/bin/env python

import urllib2
import re
import random
import math
from PIL import Image
from cStringIO import StringIO


# List of all categories of hubble images
HUBBLE_ALL = "http://hubblesite.org/gallery/album/entire/npp/all/"
HUBBLE_NEBULA = "http://hubblesite.org/gallery/album/nebula/npp/all/"
HUBBLE_UNIVERSE = "http://hubblesite.org/gallery/album/the_universe/npp/all/"
HUBBLE_EXOTIC = "http://hubblesite.org/gallery/album/exotic/npp/all/"
HUBBLE_GALAXY = "http://hubblesite.org/gallery/album/galaxy/npp/all/"
HUBBLE_SOLAR_SYSTEM = "http://hubblesite.org/gallery/album/solar_system/npp/all/"
HUBBLE_STARS = "http://hubblesite.org/gallery/album/star/npp/all/"


# SETTINGS TO CHANGE

# Change what url to open to change types of pictures (ex. "HUBBLE_ALL", "HUBBLE_STARS")
HUBBLE_CAT_TO_LOAD = HUBBLE_NEBULA
# The size (in pixels) each separate image will be
IMG_SIZE = 300

# Stores beginning of url
HUBBLE_URL_FRONT = "http://imgsrc.hubblesite.org/hu/db/images/hs-"
# Image sizes
SMALL_URL = "-small_web.jpg"
MED_URL = "-web.jpg"
LARG_URL = "-large_web.jpg"
XLARG_URL = "-xlarge_web.jpg"


# Gets all the images from the hubble site parsing the html
def loadImages():
    r = urllib2.urlopen(HUBBLE_CAT_TO_LOAD).read()
    res = re.compile("pr(\d\d\d\d)0(\d\d)(\w)")
    img_keys = re.findall(res, r)
    img_keys = list(set(img_keys))
    return img_keys


# Create a hubble image url depending on size and key
def getImageURL(img_key, size):
    return HUBBLE_URL_FRONT + img_key[0] + '-' + img_key[1] + '-' + img_key[2] + size


# Get image from url and return as PIL image
def getImage(url):
    try:
        img_file = urllib2.urlopen(url)
        im = StringIO(img_file.read())
        image = Image.open(im)
    except urllib2.HTTPError:
        return None
    return image


# Simple function to make 2 steps into 1
def getImageFromURL(img_key, size):
    url = getImageURL(img_key, size)
    return getImage(url)


def main():
    img_keys = loadImages()
    img_keys.sort()

    # Find square to the amount of images.
    size = int(math.floor(math.sqrt(len(img_keys))))
    coll = Image.new("RGB", (size * IMG_SIZE, size * IMG_SIZE))

    # List of indexs
    index_list = list(range(0, size * size))

    index = 0
    for i in range(size):
        for j in range(size):
            # Get Random index
            ind = index_list[random.randint(0, len(index_list) - 1)]
            index_list.remove(ind)
            # Create PIL Image
            image = getImageFromURL(img_keys[ind], MED_URL)
            if image:
                # Resize the image
                image = image.resize((IMG_SIZE, IMG_SIZE))
                # Paste the image onto the large canvas
                coll.paste(image, (i * IMG_SIZE, j * IMG_SIZE))
                print "completed " + str(index + 1) + "/" + str(size * size)
                index += 1
            else:
                j -= 1

    coll.show()
    # Save image to wherever
    coll.save("hubble.jpeg", "jpeg")


if __name__ == '__main__':
    main()
