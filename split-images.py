# Quick and easy code that splits images in the bare-skin folder between training, validation and testing folders

import splitfolders
input_folder = '/home/abby/object-detection-sample-python/images/Skin/bare-skin'

# ratio is in (training, validation, testing) format
splitfolders.ratio(input_folder, output='/home/abby/object-detection-sample-python/images/Skin/grouped-bare-skin', ratio=(.7, .2, .1))