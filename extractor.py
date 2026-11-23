from email import policy
from email.parser import BytesParser
from email.utils import parseaddr
import re  

def extract(path):
    with open(path, "rb") as email_file:
        msg = BytesParser(policy=policy.default).parse(email_file)

    data = {
        "date": msg["Date"],
        "from": msg["From"],
        "from-name": parseaddr(msg["From"])[0] if msg["From"] else None, 
        "from-email": parseaddr(msg["From"])[1] if msg["From"] else None,
        "to": msg["To"],
        "subject": msg["Subject"],
        "return-path":msg["Return-Path"],
        "return-path-email": parseaddr(msg["Return-Path"])[1] if msg["Return-Path"] else None,
        "reply-to": msg["Reply-To"],
        "reply-to-email": parseaddr(msg["reply-to"])[1] if msg["reply-to"] else None,
        "body": None, 
        "authentication-results": msg.get_all("Authentication-Results") or [],
        "dkim-signature": msg["DKIM-Signature"],
        "received": msg.get_all("Received") or [],
        "jumps": [],
    }

    body = msg.get_body(preferencelist=("html", "plain"))
    if body is not None:
        data["body"] = body.get_content()

    auth = {"spf": None, "dkim": None, "dmarc": None}
    results = data["authentication-results"]
    if results:       
        trusted = results[0] #Only trust the first AuthResult since spoofed results would be under     

        found_spf = re.findall(r"\bspf=(\w+)", trusted)
        auth["spf"] = found_spf[0] if found_spf else None

        found_dkim = re.findall(r"\bdkim=(\w+)", trusted)
        auth["dkim"] = found_dkim[0] if found_dkim else None

        found_dmarc = re.findall(r"\bdmarc=(\w+)", trusted)
        auth["dmarc"] = found_dmarc[0] if found_dmarc else None
    data["auth"] = auth

    for received in data["received"]:
        jump = {}   

        jump["raw"] = received

        jump["date"] = received.split(";")[-1].strip()

        jump["ip"] = re.findall(r"\[([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\]", received)

        found_from = re.findall(r"\bfrom\s+(\S+)", received)

        jump["from"] = found_from[0] if found_from else None

        found_by = re.findall(r"\bby\s+(\S+)", received)
        jump["by"] = found_by[0] if found_by else None

        data["jumps"].append(jump)

    return data
