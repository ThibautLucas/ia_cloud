import cv2
def load_image(image_path):
    """
    Load the image using opencv
    :param image_path: <String> Path of input_image
    """
    coloured_image = cv2.imread(image_path)
    grey_image = cv2.cvtColor(coloured_image, cv2.COLOR_BGR2GRAY)
    print('image matrix size: ', grey_image.shape)
    print('\n First 5 columns and rows of the image matrix: \n', grey_image[:5, :5])
    cv2.imwrite('TopLeft5x5.jpg', grey_image[:5, :5])
    return grey_image

input_image = load_image('tortue.jpg')


def convolve2d(image, kernel):
    """
    This function which takes an image and a kernel and returns the convolution of them.

    :param image: a numpy array of size [image_height, image_width].
    :param kernel: a numpy array of size [kernel_height, kernel_width].
    :return: a numpy array of size [image_height, image_width] (convolution output).
    """
    # Flip the kernel
    kernel = np.flipud(np.fliplr(kernel))
    # convolution output
    output = np.zeros_like(image)

    # Add zero padding to the input image
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    image_padded[1:-1, 1:-1] = image

    # Loop over every pixel of the image
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y, x]=(kernel * image_padded[y: y+3, x: x+3]).sum()

    return output

# kernel to be used to get sharpened image
image_edge1 = convolve2d(input_image,kernel=np.array([[-1, -1, -1], [-1, 4, -1],[-1, -1, -1]]))
cv2.imwrite('blur.jpg', image_edge1)

image_edge1 = convolve2d(input_image,kernel=np.array([[0, 0.5, 0], [0.5, 0.5, 0.5],[0, 0.5, 0]]))
cv2.imwrite('blur.jpg', image_edge1)