# Converts each JPG image in my Skin folder to a CSV file with RGB values for each pixel. This makes it compatible
# with Google Cloud buckets, which are useful to train a custom TensorFlow model.
# This code takes a long time to run, so patience is required.

from PIL import Image
import numpy as np
from os import walk

pics = []


for filenames in walk('/home/abby/object-detection-sample-python/images/Skin/'):
    pics.extend(filenames)
    break

import csv

for m in range(len(pics[2])):
    img = Image.open(pics[0]+pics[2][m])
    imageToMatrix = np.asarray(img)
    print(pics[0]+pics[2][m])

    with open('/home/abby/object-detection-sample-python/images/SkinCSV/' + pics[2][m] + '.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerows(imageToMatrix)
        print('we did it')