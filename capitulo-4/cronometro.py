import time

seg = int(input('Quantos segundos: \n'))

for i in range(seg, -1, -1):
    print(i)
    time.sleep(1)


