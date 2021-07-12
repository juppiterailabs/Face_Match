import cv2
from matplotlib import pyplot as plt
from Libraries.ExtractKeypoints.ExtractKeypoints import extractKeypoints


def match(image_one, image_two):
    img1 = cv2.imread(image_one, cv2.IMREAD_GRAYSCALE)
    _, des1 = extractKeypoints(img1)
    img2 = cv2.imread(image_two, cv2.IMREAD_GRAYSCALE)
    _, des2 = extractKeypoints(img2)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(bf.match(des1, des2), key=lambda match: match.distance)

    score = 0
    for match in matches:
        score += match.distance

    return 100-(score / len(matches))

if __name__ == '__main__':
    '''
    Configuration
    '''
    res = match('Data/signature.jpg', 'Data/ref-signature.jpg')
    print(res)
