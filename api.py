from facematch.face import match
import signature
import utils
import numpy as np

def match_images(img_one: bytes, img_two: bytes) :
    mx = utils.read_config()["MAX_SIZE"]
    try:
        if len(img_one) > mx or len(img_two) > mx:
            raise Exception
        result, distance, _ = match(img_one, img_two)
        return {'result':str(result), 'distance': distance}
    except Exception:
        return None

def match_signatures(img_one: bytes, img_two: bytes) :
    mx = utils.read_config()["MAX_SIZE"]
    try:
        if len(img_one) > mx or len(img_two) > mx:
            raise Exception
        with open('examples/sig_test_1.jpg','wb') as f:
            f.write(img_one)
        with open('examples/sig_test_2.jpg','wb') as f:
            f.write(img_two)
        result = signature.match('examples/sig_test_1.jpg', 'examples/sig_test_2.jpg')
        return {'result':str(result)}
    except Exception:
        return None

    # f = open('out.png', 'wb')
    # f.write(data)
    # f.close()
