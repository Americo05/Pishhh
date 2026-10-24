from email import policy
from email.parser import BytesParser

def extract():
    with open("Samples/email.eml", "rb") as email: #rb for the binary mode
        msg = BytesParser(policy=policy.default).parse(email) #default policy is used to parse the email message

    dados = {
    "date": msg["Date"],
    "from": msg["From"],
    "to": msg["To"],
    "subject": msg["Subject"],
    "return-path": msg["Return-Path"],
    "body": msg.get_body(preferencelist=("html", "plain")).get_content(),
    "authentication-results": msg["Authentication-Results"]
    }
    return dados