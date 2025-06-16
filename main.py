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