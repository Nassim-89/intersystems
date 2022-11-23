
import re


def clean_email(text):
    groups = re.findall(r'^From:(.*?)To:(.*?)Subject:(.*?)$(.*?)(?=^From:|\Z)', text, flags=re.DOTALL | re.M)
    d = {}
    for g in groups:
        d = {'email_from': g[0].strip(), 'email_to': g[1].strip(), 'subject': g[2].strip(), 'message': g[3].strip()}

    return d
