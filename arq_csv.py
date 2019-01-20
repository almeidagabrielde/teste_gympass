import csv
lista = []
with open('test_f1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for linha in spamreader:
        lista.append(linha)
print(lista[1])
print(lista[1][1])