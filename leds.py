n = int(input())

for i in range(n):
    leds = 0
    entrada = input()
    for indice in range(len(entrada)):
        if entrada[indice] == '1':
            leds += 2
        elif entrada[indice] == '7':
            leds += 3
        elif entrada[indice] == '4':
            leds += 4
        elif entrada[indice] == '2' or entrada[indice] == '3' or entrada[indice] == '5':
            leds += 5
        elif entrada[indice] == '6' or entrada[indice] == '9' or entrada[indice] == '0':
            leds += 6
        elif entrada[indice] == '8':
            leds += 7
    print('{} leds'.format(leds))