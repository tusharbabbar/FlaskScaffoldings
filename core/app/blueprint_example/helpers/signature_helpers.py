import hmac
import hashlib
import urllib
import base64
from app import app
from app.exceptions import NoSignatureException
import time

KEY = app.config['API_SIGNING_KEY']

def create_signature(signed, args):
    '''
    signed : csv of the signed arguments.
    args : dict of the arguments.
    '''
    if signed:
        payload = []
        for key in signed.split(','):
            tup = (key, args[key])
            payload.append(tup)
        payload = urllib.urlencode(payload)
        hmac_obj = hmac.new(KEY, payload, hashlib.sha1)
        signature = base64.encodestring(hmac_obj.digest()).strip()
        return signature
    raise Exception('signed cannot be empty')

def validate_args(args):
    if args.get('signed') and args.get('signature'):
        signature = create_signature(args.get('signed'), args)
        if signature == args.get('signature'):
            return True
    raise NoSignatureException('args must contain signed and signature')

def create_temporary_key(*args, **kwargs):
    args_string = '+'.join(map(str,args)) + str(time.time())
    hmac_obj = hmac.new(KEY, args_string, hashlib.sha1)
    return base64.b64encode(hmac_obj.digest()).strip()

