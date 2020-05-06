plik = 'pliktekstowy.txt'
openfile = open(plik, 'r')
savefile = 'pliktekstowy2.txt'
openfile2 = open(savefile, 'w')


def reading_file(plik):
    lista = []
    file = plik.readlines()
    for line in file:
        if line[-1] == '\n':
            lista.append(line[:-1])
        else:
            lista.append(line)
    into_str = ''.join(lista)  # Convert from list into string

    n = 26  # New line every 26 chars
    lines = []
    for i in range(0, len(into_str), n):
        lines.append(into_str[i:i + n])
    new_lines = '\n'.join(lines)

    '''for elem in new_lines:
        if elem == ' ':
            elem.replace(" ", "")
            openfile2.write(new_lines)'''
    return new_lines


print(reading_file(openfile))
