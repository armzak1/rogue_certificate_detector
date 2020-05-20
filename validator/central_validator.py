from bottle import run, post, request, response
import json
import ssl 
import hashlib
from validators import CentralValidator, DistantValidator
import utils

cv = CentralValidator(['http://localhost:8081', 'http://localhost:8082'])

@post('/check_certificate', methods=['POST'])
def verify_central():
    body_dict = json.load(request.body)
    url, cert_fingerprint = body_dict['url'], body_dict['cert_fingerprint']
    url = utils.normalize_url(url)
    cert_fingerprint = utils.normalize_cert_fingerprint(cert_fingerprint)
    try:
        is_valid = cv.verify(url, cert_fingerprint)
    except Exception as e:
        return str(json.dumps({'Result': 'Internal error \n {}'.format(e)}))
        
    response.status = 200
    if is_valid:
        return str(json.dumps({'Result': 'OK'}))
    else:
        return str(json.dumps({'Result': 'Cert Mismatch'}))

run(host='localhost', port=8080)




