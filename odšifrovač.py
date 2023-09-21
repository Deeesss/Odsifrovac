hekovanie = ""
print("Sifrovana sprava: ", hekovanie)
sifra = ""
posun = -1

for znak in hekovanie:
    i = ord(znak)
    i = i + posun
    if(i < ord("a")):
        i = i + 26
    znak = chr(i)
    sifra = sifra + znak

print("sifra:", sifra)