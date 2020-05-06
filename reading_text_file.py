plik = 'pliktekstowy.txt'
podajplik = open(plik, 'r')
plik2 = 'pliktekstowy2.txt'
podajplik2 = open(plik2, 'w')


def reading_file(plik):
    lista = []
    file = plik.readlines()
    for line in file:
        if line[-1] == '\n':
            lista.append(line[:-1])
        else:
            lista.append(line)

    into_str = ''.join(lista)
    newline_into_str = into_str[:26] + '\n' + into_str[26:]
    podajplik2.write(newline_into_str)
    return newline_into_str

print(reading_file(podajplik))
