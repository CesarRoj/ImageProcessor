from matplotlib import pyplot as plt
from matplotlib import cm
from skimage import data
from skimage.feature import blob_dog, blob_log,blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
#create readme for this later


# This code is using the glob module to find the file path of an image
# file named "second_sky.gif" in the current directory. 
# The glob function returns a list of file paths that match the specified
# pattern, so [0] is used to select the first path in the list 
# (assuming there is only one match).

# The next line reads the image file using the imread function 
# from the skimage.io module, and it converts the image to
# grayscale by setting as_gray=True. The resulting grayscale 
# image is stored in the image variable.

# The blob_log function from the skimage.feature module is
# then used to detect blobs (i.e., bright spots) in the
# grayscale image using the Laplacian of Gaussian (LoG) method. 
# The max_sigma, num_sigma, and threshold parameters control the 
# sensitivity of the blob detection algorithm. 
# The blobs_log variable contains the (y, x, r) coordinates of the 
# detected blobs, where y and x are the blob centers and r is the radius.

# The next line computes the actual radii of the blobs by 
# multiplying the values in the third column of blobs_log by the 
# square root of 2. Finally, the code prints the number of detected 
# blobs to the console

#will convert the image to a matrix
#once cell will equate to on
# e part in the matrix
example_file = glob.glob(r"second_sky.gif")[0]

image = imread(example_file, as_gray=True)

blobs_log = blob_log(image, max_sigma=60, num_sigma=60, threshold =.1)
#compute radii in the 3rd column
blobs_log[:,2] = blobs_log[:,2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counter: " ,numrows)


fig, ax = plt.subplots(1, 1)
plt.imshow(image, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)
    
plt.show()