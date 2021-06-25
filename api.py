from facematch.face import match
import config

def match_images(img_one: bytes, img_two: bytes) :
    try:
        if len(img_one) > config.MAX_SIZE or len(img_two) > config.MAX_SIZE:
            raise Exception
        result, distance, _ = match(img_one, img_two)
        return {'result':str(result), 'distance': distance}
    except Exception:
        return None


    # f = open('out.png', 'wb')
    # f.write(data)
    # f.close()
