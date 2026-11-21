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
