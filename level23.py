# Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

# The pixels in the input image are represented as integers.
# The algorithm distorts the input image in the following way:
# Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

def solution(image):
    mat_n = []

    for j in range(1, len(image)-1):
        mat_n.append([])
        nest = mat_n[j-1]

        for k in range(1, len(image[j])-1):

            nest.append(((image[j-1][k-1])+(image[j-1][k])+(image[j-1][k+1])+(image[j][k-1])+(image[j][k])+(image[j][k+1])+(image[j+1][k-1])+(image[j+1][k])+(image[j+1][k+1]))//9)

    return mat_n