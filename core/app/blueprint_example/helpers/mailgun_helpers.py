import requests
from app import app

base_url = "https://api.mailgun.net/v3/{domain}".format(domain = app.config["MAILGUN_DOMAIN"])
api_key = app.config["MAILGUN_KEY"]

def _post_to_mailgun(data):
    request_url = base_url + '/messages'
    response = requests.post(request_url, auth = ('api', api_key), data = data)
    if response.status_code >= 200 and response.status_code < 300:
        return True 

def send_html_mail(_from, to, subject, body, cc = None, bcc = None, set_reply_to = None):
    '''
    _from : string email_id
    to : string email_id
    subject : string subject line
    body : string. **Should be HTML
    cc : list of email_id strings
    bcc : list of email_id strings
    '''
    data = {}
    data['from'] = _from
    data['to'] = to
    data['subject'] = subject
    data['html'] = body
    if cc:
        cc = ','.join(cc)
        data['cc'] = cc
    if bcc:
        bcc = ','.join(bcc)
        data['bcc'] = bcc
    if set_reply_to:
        data['h:Reply-To'] = set_reply_to
    return _post_to_mailgun(data)
