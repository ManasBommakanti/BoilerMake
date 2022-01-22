import http.client
import numpy as np
import mnist
from PIL import Image
from numpy import *


class Conv:
    # Convolution layer

    def __init__(self, num_filters):
        self.num_filters = num_filters

        # filters is a 3d array with dimensions (num_filters, 3, 3)
        # We divide by 9 to reduce the variance of our initial values
        self.filters = np.random.randn(num_filters, 3, 3) / 9

    def iterate_regions(self, image):
        h, w, c = image.shape

        for i in range(h - 2):
            for j in range(w - 2):
                im_region = image[i:(i + 3), j:(j + 3)]
                yield im_region, i, j

    def forward(self, input):
        h, w, c = input.shape
        output = np.zeros((h - 2, w - 2, self.num_filters))

        for im_region, i, j in self.iterate_regions(input):
            #print(str(im_region) + " " + str(i) + " " + str(j))
            #print(im_region)
            #print(self.filters)
            #print(mult)
            output[i, j] = np.dot(im_region, self.filters).sum()

        return output


img = Image.open('apple_test.jpeg')
img = img.resize((28, 28))
imgGray = img.convert('L')
imgGrayArray = array(img)

conv = Conv(8)
print(conv.forward(imgGrayArray).shape)
