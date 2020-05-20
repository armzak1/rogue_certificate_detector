let getCertUrl = async (urlTested, httpHeadMethod=false) => {
  let response      = null
  let response_data = null
  let cert          = null

  const listener = async (details) => {
    browser.webRequest.onHeadersReceived.removeListener(listener)
    const securityInfo = await browser.webRequest.getSecurityInfo(details.requestId, { certificateChain: true })
    if (securityInfo.state === 'secure' || securityInfo.state === 'weak') {
      console.log(securityInfo.certificates);
      let data = {url: urlTested, cert_fingerprint: securityInfo.certificates[0].fingerprint.sha1}
      checkCertRemote(data).then((res) => res.json()).then(body => {
        console.log(body['Result']) //for debugging
        if(body['Result'] != 'OK'){
          var mismatchNotification = "mismatch-notification"
          browser.notifications.create(cakeNotification, {
            "type": "basic",
            "iconUrl": "icons/379743.png",
            "title": "Security Threat!",
            "message": "Certificate Mismatch. Possible interception of the traffic."
          });
        }
        
      });
    }
  }

  browser.webRequest.onHeadersReceived.addListener(listener,
    { urls: [urlTested], types: ['xmlhttprequest'] },
    ['blocking']
  )

  try {
    if (httpHeadMethod) {
      fetchInit = { method: 'HEAD' }
    } else {
      fetchInit = {}
    }
    response = await fetch(urlTested, fetchInit)

    const contentType = response.headers.get('content-type')
    if(contentType && contentType.includes('application/json')) {
      response_data = await response.json()
    } else {
      response_data = await response.text()
    }
  } catch (e) {
    // console.error(e)
  }

  return { data: response_data, cert: cert, response: response }
}

let checkCertRemote = async (data) => {
  console.log("Sending Request with", data);
  return fetch("http://localhost:8080/check_certificate", {
        method: 'POST', 
        body: JSON.stringify(data)
  });
}

let updateListener = (tabId, changeInfo, tabInfo) => {
  if (changeInfo.url){
    getCertUrl(changeInfo.url);
    console.log('Changes', changeInfo.url);
  }
}

browser.tabs.onUpdated.addListener(updateListener)