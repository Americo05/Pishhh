import extractor

dados = extractor.extract()
print(dados["date"])
print(dados["from"])
print(dados["to"])
print(dados["subject"])
print(dados["return-path"])
print(dados["body"])
print(dados["authentication-results"])
