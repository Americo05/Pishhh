import extractor
import analyzer

data = extractor.extract("Samples/email.eml")      

print("Date:", data["date"])
print("From:", data["from"])
print("To:", data["to"])
print("Subject:", data["subject"])
print("Return-path:", data["return-path-email"])
print("--Received Data--",)
for jump in data["jumps"]:  
    print(jump["from"], "->", jump["by"])
    print(jump["ip"])
    print(jump["date"])
print("-----------------")
print("From matches Return-path:", analyzer.return_path_matches_from(data))
