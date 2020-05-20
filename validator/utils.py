def normalize_cert_fingerprint(cert_fingerprint):
    return cert_fingerprint.replace(':', '').lower()


def normalize_url(url):
    return url.replace('https://', '').split('/')[0]