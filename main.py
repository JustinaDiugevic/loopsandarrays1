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