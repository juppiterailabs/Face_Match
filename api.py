from facematch.face import match
import utils

def match_images(img_one: bytes, img_two: bytes) :
    mx = utils.read_config()["MAX_SIZE"]
    try:
        if len(img_one) > mx or len(img_two) > mx:
            raise Exception
        result, distance, _ = match(img_one, img_two)
        return {'result':str(result), 'distance': distance}
    except Exception:
        return None


    # f = open('out.png', 'wb')
    # f.write(data)
    # f.close()
