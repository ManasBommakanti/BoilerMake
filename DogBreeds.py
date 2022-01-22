import http.client
import numpy as np
from PIL import Image
from numpy import*

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
            output[i, j] = np.sum(im_region * self.filters, axis=(1, 2))

        return output


conn = http.client.HTTPSConnection("api.thedogapi.com")

headers = { 'x-api-key': "9207caa6-f2dc-4493-8d61-5cf3ad0e3c3f" }

conn.request("GET", "/v1/breeds?attach_breed=0", headers=headers)

res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

img = Image.open('apple_test.jpeg')
imgGray = img.convert('L')
imgGrayArray = array(img)
imgGray.save('test_gray.jpg')

conv = Conv(3)
print(conv.forward(imgGrayArray).shape)

