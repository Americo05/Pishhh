import re  
def return_path_matches_from(data):
    if not data["return-path-email"] or not data["from-email"]:
        return None
    else:
        domainf = data["from-email"].split("@")[-1].lower() #Split the email in 2 and takes the domain part after the @ symbol
        domainr = data["return-path-email"].split("@")[-1].lower()
        if domainf != domainr:
            return False
        else:
            return True

def reply_to_matches_from(data):
    if not data["reply-to-email"] or not data["from-email"]:
        return None
    else:
        domainr = data["reply-to-email"].split("@")[-1].lower()
        domainf = data["from-email"].split("@")[-1].lower()
        if domainr != domainf:
            return False
        else:
            return True

def auth_analyzer(data):
    errors={"fail": 3, 
            "softfail": 2,
            "neutral": 1,
            "none": 1,
            "temperror": 1,
            "permerror": 1,
            "policy": 1
            }
    #Dictionary from 1 to 3 1-Weak 2-Alarming 3-Critical 
    for key, value in data["auth"].items():
        if value == "pass":
            print("[OK]",key.upper(),": pass")
            continue

        if value is None:
            print("[INFO]",key.upper(),": no result found")
        elif value in errors and errors[value] == 3:
            print("[CRITICAL]",key.upper(),":",value," The email failed authentication and may be spoofed")
        elif value in errors and errors[value] == 2:
            print("[WARNING]",key.upper(),":",value," The domain does not fully authorize this sender")
        elif value in errors and errors[value] == 1:
            print("[LOW]",key.upper(),":",value," Weak signal; the domain may lack protection or had an error")
        else:
            print("[UNKNOWN]",key.upper(),":",value," is not a recognized result. Check the original header")