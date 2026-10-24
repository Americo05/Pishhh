from email import policy
from email.parser import BytesParser

def extract():
    with open("Samples/email.eml", "rb") as email: #rb for the binary mode
        msg = BytesParser(policy=policy.default).parse(email) #default policy is used to parse the email message

    print(msg["subject"]) #prints the subject of the email
    print(msg["from"]) #prints the sender of the email
    print(msg["to"]) #prints the recipient of the email
    print(msg.get_content_type()) #prints the content type of the email
    print(msg.get_body("text/plain")) #prints the body of the email
