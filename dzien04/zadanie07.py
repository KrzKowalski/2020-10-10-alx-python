napis = "ala ma kota, ola ma psa, robert ma żółwia, a ula ma chomika"

samogloski = [ "a", "e", "o", "i", "u", "y", "ó" ]

ile_samoglosek = 0

for litera in napis:
    if litera in samogloski:
        ile_samoglosek += 1

print(f"Samoglosek: {ile_samoglosek}")