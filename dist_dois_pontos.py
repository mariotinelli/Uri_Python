from math import sqrt

linha1 = input().split()
linha2 = input().split()

linha1 = [float(i) for i in linha1]
linha2 = [float(i) for i in linha2]

distancia = sqrt(((linha2[1]-linha1[1])**2)+((linha2[0]-linha1[0])**2))

print('{:.4f}'.format(distancia))
