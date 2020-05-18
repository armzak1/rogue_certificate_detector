from bottle import run, post, request, response
import json
import ssl 
import hashlib

@post('/check_certificate', methods=['POST'])
def test():
    body_dict = json.load(request.body)
    url, cert_fingerprint = body_dict['url'], body_dict['cert_fingerprint']
    cert_fingerprint = cert_fingerprint.replace(':', '').lower()
    url = url.replace('https://', '').split('/')[0]
    cert = ssl.PEM_cert_to_DER_cert(ssl.get_server_certificate((url, 443)))
    cert = hashlib.sha1(cert).hexdigest()
    print(cert_fingerprint)
    print(cert)
    response.status = 200
    if cert == cert_fingerprint:
        return str(json.dumps({'Result': 'OK'}))
    else:
        return str(json.dumps({'Result': 'Cert Mismatch'}))

run(host='localhost', port=8080)
