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
            output[i, j] = np.dot(im_region, self.filters).sum()

        return output


class Pool:
    # A Max Pooling layer using a pool size of 2.

    def iterate_regions(self, image):
        h, w, _ = image.shape
        new_h = h // 2
        new_w = w // 2

        for i in range(new_h):
            for j in range(new_w):
                im_region = image[(i * 2):(i * 2 + 2), (j * 2):(j * 2 + 2)]
                yield im_region, i, j

    def forward(self, input):
        h, w, num_filters = input.shape
        output = np.zeros((h // 2, w // 2, num_filters))

        for im_region, i, j in self.iterate_regions(input):
            output[i, j] = np.amax(im_region, axis=(0, 1))

        return output


img = Image.open('apple_test.jpeg')
img = img.resize((28, 28))
imgGray = img.convert('L')
imgGrayArray = array(img)

conv = Conv(10)
convOutput = conv.forward(imgGrayArray)  # 26, 26, 10
pool = Pool()
poolOutput = pool.forward(convOutput)  # 13, 13, 10

print(poolOutput.shape)
