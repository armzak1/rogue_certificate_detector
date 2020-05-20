from bottle import run, post, request, response
import json
import ssl 
import hashlib
import requests

class CentralValidator:
    def __init__(self, distant_validator_urls):
        self.distant_validator_urls = distant_validator_urls
    
    def verify(self, url, cert_fingerprint):
        is_valid = True
        for dv in self.distant_validator_urls:
            dv_response = self.request_distant_validation(dv, url, cert_fingerprint)
            is_valid &= dv_response
        return is_valid

    def request_distant_validation(self, dvurl, url, cert):
        resp = requests.post(dvurl + '/check_certificate', data = str(json.dumps({'url': url, 'cert_fingerprint': cert})))
        print(resp.text)
        if resp.status_code == 200:
            resp_dict = resp.json()
            if 'is_valid' in resp_dict:
                is_valid = resp.json()['is_valid']
                return is_valid
        raise Exception('Invalid Response from DV: {}'.format(dvurl))


class DistantValidator:
    def __init__(self):
        pass

    def verify(self, url, cert_fingerprint):
        cert = ssl.PEM_cert_to_DER_cert(ssl.get_server_certificate((url, 443)))
        cert = hashlib.sha1(cert).hexdigest()
        print(cert_fingerprint)
        print(cert)
        return cert == cert_fingerprint



    

        


    