from bottle import run, post, request, response
import json
import ssl 
import hashlib
from validators import CentralValidator, DistantValidator
import utils

dv = DistantValidator()

@post('/check_certificate', methods=['POST'])
def verify_distant():
    body_dict = json.load(request.body)
    url, cert_fingerprint = body_dict['url'], body_dict['cert_fingerprint']
    url = utils.normalize_url(url)
    cert_fingerprint = utils.normalize_cert_fingerprint(cert_fingerprint)
    is_valid = dv.verify(url, cert_fingerprint)
    response.status = 200
    return str(json.dumps({'is_valid': is_valid}))

run(host='localhost', port=8081)




