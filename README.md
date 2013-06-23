# Hubble Image Stitcher
Creates a large square image from a bunch of small hubble images

### Insturctions
- Just run python script.
- Saves Images to whichever directory script is located.
- Change Change HUBBLE_CAT_TO_LOAD variable to category wanted.
- Change IMG_SIZE variable to whatever size you want each picture to be.
- size of larger picture is determined by square root of total amount of pictures * IMG_SIZE
    - If you use HUBBLE_ALL, there are about 1225 images. sqrt(1225) = 35. 35 * image size of 100px = 3500 pixels


\* Requires some imports