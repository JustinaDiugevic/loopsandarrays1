import random

for i in range(10):
    print("labas")
for i in range(10):
    print(i)

augalai = ['levanda', 'pusis', 'egle', 'lelija', 'meta', 'aguona', 'palme', 'roze', 'tuja', 'alyva']
print(augalai)
for augalas in augalai:
    print(augalas)

for augalas in reversed(augalai):
    print(augalas)



for i in range(10, 51, 2):
    print(i)


for i in range(10, 51, 2):
    if i % 10 == 0:
        continue
    print(i)

print(augalai)
count = 0
for i in range(0, 21):
    if i % 2 == 0:
        count += 1
print("Poriniai", count)


count = 0
for i in range(len(augalai)):
    if len(augalai[i]) <= 5:
        count += 1
print("Trumpi", count)


count = 0
for augalas in augalai:
    if len(augalas) >= 7:
        count += 1
print("Ilgi", count)

for augalas in augalai:
    if 5 <= len(augalas) <= 10:
        count += 1
print("Vidutiniai", count)

skaiciai = [random.randint(0, 300) for _ in range(300)]

count = 0

for skaicius in skaiciai:
    if skaicius > 150:
        count += 1
    if skaicius > 275:
        print("[" + str(skaicius) + "]", end=' ')
    else:
        print(skaicius, end=' ')
print()


skaiciai = [i for i in range(1, 3001) if i % 77 == 0]
print(*skaiciai, sep=',')

for i in range(25):
    print('* ' * 25)



while True:
    result = random.randint(0, 1)
    if result == 0:
        print("H")
        break
    else:
        print("S")


count = 0
while count < 3:
    result = random.randint(0, 1)
    if result == 0:
        count += 1
        print("H")
    else:
        print("S")


count = 0
while count < 3:
    result = random.randint(0, 1)
    if result == 0:
        print("H")
        count += 1
else:
        print("S")
        count = 0


print("6 sunkesniu uzduotis".center(60, "_"))



petro_count = 0
kazio_count = 0

while petro_count < 222 and kazio_count < 222:
    petro_taskai = random.randint(10, 20)
    kazio_taskai = random.randint(5, 25)

    petro_count += petro_taskai
    kazio_count += kazio_taskai

    if petro_taskai > kazio_taskai:
        winner = "Petras"
    elif kazio_taskai > petro_taskai:
        winner = "Kazys"
    else:
        winner = "Lygiosios"
print(f"Petro taskai: {petro_taskai}, Kazio taskai: {kazio_taskai}. Laimejo: {winner}")

print("8 sunkesni uzduotis".center(60, "_"))

ikalta_count = 0
smugiai_count = 0

vinys = 5
ilgis = 85

for vinis in range(1, vinys + 1):
    ikalta_count = 0
    smugiai_count = 0
    while ikalta_count < ilgis:
        smugio_gylis = random.randint(5, 20)
        ikalta_count += smugio_gylis
        smugiai_count += 1


    print(f"{vinis} vinis ikaltas per {smugiai_count} smūgius.")

for vinis in range(1, vinys + 1):
    ikalta_count = random.randint(0, 1)
    smugiai_count = 0
    while ikalta_count < ilgis:
        smugio_gylis = random.randint(20, 30)
        ikalta_count += smugio_gylis
        smugiai_count += 1
    print(f"{vinis} vinis ikaltas per {smugiai_count} smūgius.")

print("4 sunkesni uzduotis".center(60, "_"))

dydis = 25

for i in range(dydis):
    for x in range(dydis):
        if i == x or x == dydis - i - 1:
            print("?", end=" ")
        else:
            print("*", end=" ")
    print()

print("7 uzduotis".center(60, "_"))

eilutes = 21
vidurys = eilutes // 2

for i in range(vidurys + 1):
    tarpai = ' ' * (vidurys - i)
    zvaigzdutes = '*' * (2 * i + 1)
    print(tarpai + zvaigzdutes)


for i in range(vidurys - 1, -1, -1):
    tarpai = ' ' * (vidurys - i)
    zvaigzdutes = '*' * (2 * i + 1)
    print(tarpai + zvaigzdutes)

