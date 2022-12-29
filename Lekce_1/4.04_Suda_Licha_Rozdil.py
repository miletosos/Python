cisla = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]
sude = []
liche = []
while cisla:
    cislo = cisla.pop()
    if cislo % 2 == 0:
        sude.append(cislo)
    else:
        liche.append(cislo)

print("sudá:", sude)
print("lichá:", liche)

soucet_suda = 0
soucet_licha = 0

while sude:
    cislo = sude.pop()
    soucet_suda = cislo + soucet_suda

while liche:
    cislo = liche.pop()
    soucet_licha = cislo + soucet_licha

rozdil = soucet_licha - soucet_suda
if rozdil < 0:
    rozdil = rozdil * -1

print("Rozdíl je:", rozdil)