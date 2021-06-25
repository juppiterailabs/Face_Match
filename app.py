from flask import Flask, jsonify, make_response, request
import hashlib
from werkzeug.middleware.proxy_fix import ProxyFix
import utils
from api import match_images
from datetime import datetime

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in utils.read_config()["ALLOWED_EXTENTIONS"]

def auth(token, ip):
    current_date = datetime.utcnow().date()
    return hashlib.sha256(str(current_date).encode('utf-8')).hexdigest() == token and ip in utils.read_config()["REMOTE_ADDRS"]

@app.route('/')
def index():
    if not auth(request.form.get('token'), request.remote_addr):
        return make_response(f'Request is not authorised {request.remote_addr}', 403)
    
    return make_response('Server is healthy', 200)


@app.route('/match-face', methods=['POST'])
def match():
    if not auth(request.form.get('token'), request.remote_addr):
        return make_response('Request is not authorised', 403)

    img_one = request.files.get('img_one')
    img_two = request.files.get('img_two')
    if img_one and img_two and img_one.filename !='' and img_two.filename !='' and allowed_file(img_one.filename) and allowed_file(img_two.filename):
        res = match_images(img_one.read(),img_two.read())
        if not res:
            return make_response('Unable to process, Please pick different images, Size should be less than 5MB or images should contain only one face', 400)
        return jsonify(res)
    else:
        return make_response('Bad request body', 400)   


@app.route('/config', methods=['PUT','DELETE'])
def update_config():
    if not auth(request.form.get('token'), request.remote_addr):
        return make_response('Request is not authorised', 403)
    data = utils.read_config()
    updated_data = request.get_json()
    for key in data:
        item = updated_data.get(key)
        if item:
            if request.method == "PUT" and key == 'MAX_SIZE':
                data[key] = item
            elif isinstance(item, list):
                if request.method == "PUT":
                    data[key].extend(item)
                    data[key] = list(set(data[key]))
                elif request.method == "DELETE":
                    for sub_item in item:
                        try:
                            data[key].remove(sub_item)
                        except ValueError:
                            pass
            elif isinstance(item, str):
                if request.method == "PUT":
                    data[key].append(item)
                elif request.method == "DELETE":
                    try:
                        data[key].remove(item)
                    except ValueError:
                        pass
    if not data['REMOTE_ADDRS']:
        data['REMOTE_ADDRS'] = ["127.0.0.1"]
    if not data['ALLOWED_EXTENTIONS']:
        data['ALLOWED_EXTENTIONS'] = ["jpeg", "jpg", "png"]
    if not data['MAX_SIZE']:
        data['MAX_SIZE'] = 5242880

    utils.save_config(data)
    return data


if __name__ == "__main__":
    app.run()