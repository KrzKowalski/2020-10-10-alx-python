liczby = [ 1, 5, 200 ]

print(f"Przed: {liczby}")

pmax, pmin = 0, 0

for p in range( len(liczby) ):
    if liczby[ p ] < liczby[ pmin ]:
        pmin = p
    if liczby[ p ] > liczby[ pmax ]:
        pmax = p

print(f"pmin={pmin} ==> {liczby[pmin]}")
print(f"pmax={pmax} ==> {liczby[pmax]}")

liczby[pmax], liczby[pmin] = liczby[pmin], liczby[pmax]

print(f"Po: {liczby}")
