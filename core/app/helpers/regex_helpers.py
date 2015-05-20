import re

def get_emails_from_text(text):
    return re.findall('[\w|\d|\+|\_|\.]*\@[\w|\d|\+|\_|\.]*', text)
